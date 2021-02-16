import random
import time
import praw


def redditConnect():
    print("Connecting to reddit...")

    greetings = ["Howdy", "Hey there", "What's up", "How're you doin'", "Hey"]

    # set praw variables and connect to subreddit
    global sub
    global r
    global subreddit
    title = "Dedicated Shot Glass Bet Subreddit! New Gameday Thread Bot!"
    subs = ["Habs", "Devils", "TampaBayLightning", "Leafs", "StLouisBlues", "OttawaSenators", "WildHockey", "Hawks", "ColoradoAvalanche", "Coyotes"]
    postedSubs = ["Hockey", "GoldenKnights", "BostonBruins", "Penguins", "WinnipegJets", "SanJoseSharks",
                  "Predators", "AnaheimDucks", "DetroitRedWings", "LosAngelesKings", "CalgaryFlames",
                  "Canes", "FloridaPanthers", "EdmontonOilers", "NewYorkIslanders", "DallasStars", "Caps"]
    r = praw.Reddit("bot1")

    print("Posting in", len(subs), "subreddits")
    print("Already posted in", len(postedSubs), "subreddits")

    for sub in subs:
        if sub in postedSubs:
            print(sub, "is in postedSubs")
            continue
        else:
            subreddit = r.subreddit(sub)
            greet = random.choice(greetings)
            intro = greet + " /r/" + sub + "!\n\n"
            secondPara = "Some of you may recognize /r/ShotGlassBets from the previous 3 years, and those that do will be the first to recall that it was a bit of a mess. The only posting standard in place was a guideline for how to title your post and even that was not always followed to a T.\n\n"
            thirdPara = "My latest update fixes all of that. Now, posts are automatically created every morning (by me!) to help facilitate the process of finding a wagering partner. No more are the days of hoping someone sees your post title before they see someone else's, now every bet for one game will fall into the same location, making it easier than ever!\n\n"
            fourthPara = "Head on over to /r/ShotGlassBets to check it out before tonight's game!\n\n"
            fifthPara = "For those that don't know, a shot glass bet is a small wager involving two fans from two opposing teams. The fan of the losing team must send a shot glass with thei team's logo on it to the fan of the winning team, with the ultimate goal being to collect every team!"
            postText = intro + secondPara + thirdPara + fourthPara + fifthPara
            if sub == "DallasStars":
                postText = postText + "\n\n" + "Let's go Stars!"
            print(sub, "- Waiting 11min 40s to post")
            time.sleep(700)  # 11min 40sec
            print("Posting to /r/" + sub)
            subreddit.submit(title, selftext=postText, resubmit=True, send_replies=True)
            print("Posted!")


# run code
redditConnect()
