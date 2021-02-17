from datetime import date, datetime
from pytz import timezone
import requests
import time
import praw
import ast

SUB = "ShotGlassBets_Testing"
BOT = "sgb_bot"


def main():
    # set praw variables and connect to subreddit
    print("Connecting to reddit...")
    reddit = praw.Reddit(BOT, config_interpolation="basic")
    reddit.validate_on_submit = True
    subreddit = reddit.subreddit(SUB)
    print(f"Connected to: {subreddit.title}")

    removePosts(subreddit)
    postNHLThreads(subreddit)


def removePosts(subreddit):
    print("Removing posts > 1.5 days old and with 0 comments")

    # set counters to 0
    i = 0
    zeroComCount = 0

    # pull new submissions
    for submission in subreddit.new(limit=37):  # change to 30 after 1st run
        # get post info
        numCom = submission.num_comments
        postTitle = submission.title
        postAuthor = submission.author
        username = "ShotGlassBets_Bot"

        # set recency check
        unixTime = time.time()
        unixDay = 86400
        checkTime = unixTime - (unixDay * 1.5)
        createdTime = submission.created_utc

        # check if post > 1.5 days old, if not stickied, and if bot posted it
        if (
            (checkTime > createdTime) and
            (submission.stickied is False) and
            (postAuthor == username)
        ):
            i += 1

            # now see which of those posts had 0 comments and remove them
            if (numCom == 0):
                zeroComCount += 1
                submission.mod.remove()
                print(f"Removed: {postTitle}")
    print(f"{zeroComCount} of {i} posts had 0 comments\n")


def postNHLThreads(subreddit):
    print(f"Creating posts for /r/{SUB}")

    # get dates and set date formats
    today = date.today()
    longDay = str(today)
    simpleDay = f"{today.month}/{today.day}"
    timeFormat = "%I:%M %p %Z"

    # create today's URL for API call
    baseURL = "https://statsapi.web.nhl.com/api/v1"
    todaySchedURL = baseURL + "/schedule?date=" + longDay

    # pull game info
    response = requests.get(todaySchedURL)
    response = response.json()
    dates = response["dates"]
    datesString = str(dates[0])
    datesDict = ast.literal_eval(datesString)
    games = datesDict["games"]
    gameCount = 0

    # check each game to create a title and post to reddit
    for game in games:
        gameCount += 1
        rawGameDate = datetime.strptime(game["gameDate"], "%Y-%m-%dT%H:%M:%SZ")
        cleanGameDate = rawGameDate.replace(tzinfo=timezone("UTC"))
        easternGameDate = cleanGameDate.astimezone(timezone("US/Eastern"))
        cleanTime = easternGameDate.strftime(timeFormat)
        awayName = game["teams"]["away"]["team"]["name"]
        homeName = game["teams"]["home"]["team"]["name"]
        title = f"[{simpleDay}] {homeName} @ {awayName} ({cleanTime})"

        # submit post to reddit
        subreddit.submit(
            title, selftext="", url=None,
            resubmit=True, send_replies=False).mod.flair(text="NHL")
        print(f"Posted: {title}")
    print(f"{gameCount} posts submitted\n")


# run code
if __name__ == "__main__":
    main()
