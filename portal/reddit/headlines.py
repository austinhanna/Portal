import praw
r = praw.Reddit(user_agent='windows:com.itsaustinh.portal:v0.1.0 (by /u/Swagmanhanna)')
for item in r.get_top():
    print(item)
