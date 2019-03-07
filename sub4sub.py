#!/usr/bin/python
import praw
import time

reddit = praw.Reddit('bot1')

title = 'Sub4Sub, Playlist4Playlist, Comment4Comment'
post = '#Subscribe to my channel here: [My Channel](http://href.li/?https://bit.ly/2XrbqQd). \n\n Go to any video, leave a comment, and then Subscribe. \n\nI also am willing to watch your playlists in exchange for mine, comment here with your playlist URL after starting mine.\n\n I\'ll comment on one of your videos as soon as I see it!'

while (1>0):
    reddit.subreddit('sub4sub').submit(title, selftext=post)
    time.sleep(5)
    for submission in reddit.subreddit('sub4sub').new(limit=1):
        thread = reddit.submission(id=submission.id)
    time.sleep(10800)
    thread.delete()
    time.sleep(10)
