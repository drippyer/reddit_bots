import random
import praw

SUB = "Drip_Test"
REPLIES = ["If it's stupid but it works, it ain't stupid!"]


def main():

    print("Connecting to reddit...")
    reddit = praw.Reddit("stupid_bot", config_interpolation="basic")
    subreddit = reddit.subreddit(SUB)
    print(f"Connected to: {subreddit.title}")

    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    if submission.saved is False:
        print(f"Replying to: {submission.title}")
        submission.reply(random.choice(REPLIES))
        print("Replied!")

        print(f"Saving: {submission.title}")
        submission.save()
        print("Saved!\n")


if __name__ == "__main__":
    main()
