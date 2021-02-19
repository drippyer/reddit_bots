import random
import praw

BOT = "stupid_bot"
SUB = "redneckengineering"
REPLIES = ["If it's stupid but it works, it ain't stupid!"]
REPLY_TEMPLATE = '''
{}

---
^This ^comment ^was ^made ^by ^a ^bot.
^Contact ^[u/drippyer](https://www.reddit.com/user/Drippyer/)
^for ^concerns.
                 '''


def main():
    print("Connecting to reddit...")
    reddit = praw.Reddit(BOT, config_interpolation="basic")
    subreddit = reddit.subreddit(SUB)
    print(f"Connected to: {subreddit.title}")

    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    if submission.saved is False:

        reply_subtext = random.choice(REPLIES)
        reply_full = REPLY_TEMPLATE.format(reply_subtext)

        print(f"Replying to: {submission.title}")
        submission.reply(reply_full)
        print("Replied!")

        print(f"Saving: {submission.title}")
        submission.save()
        print("Saved!\n")


if __name__ == "__main__":
    main()
