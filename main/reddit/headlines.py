import praw
reddit = praw.Reddit(user_agent='Portal Reddit Module (by /u/Swagmanhanna)',
                     client_id='9EASNimdp6ItMw', client_secret="cuuiAqw8QCq3f8jDMbU0uV4uLWA")
for submission in reddit.subreddit('GlobalOffensive').hot(limit=10):
    print(submission.title.encode("utf-8"))
