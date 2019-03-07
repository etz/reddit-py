#!/usr/bin/python
import praw
import feedparser
import sys
import time

client = ""
secret = ""
user = ""
password = ""
agent = "ReutersPost20"
subreddits ['business', 'news', 'inthenews']
reddit = praw.Reddit(client_id=client, client_secret=secret, password=password, user_agent=agent, username=user)
lpt = ''

while(1>0):
	feed = feedparser.parse('http://feeds.reuters.com/reuters/businessNews')
	url = feed['entries'][0]['link']
	title = feed['entries'][0]['title']
	if (title != lpt):
		print("New post found! Approving...")
		reddit.subreddit(random.choice(subreddits)).submit(title, url=url)
		print("Posted. Goodnight ⭐")
		lpt = title
		time.sleep(16000)
