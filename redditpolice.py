#!/usr/bin/python
import praw
import sys
import time



client=""
secret=""
password=""
user=""
agent="euerkeodpa"

reddit = praw.Reddit(client_id=client, client_secret=secret, password=password, user_agent=agent, username=user)
comment = ''
reply = """ 🛑**ALERT**🛑

This account has been marked as a useless reply bot. We recommend you complain to the bot creator, where he will subsequently ignore your messages. You can also report the comment to your sub-reddit moderators to ban reply bots that don't follow the guidelines of [good bot citizenship](https://www.reddit.com/r/redditdev/comments/98vj9e/please_be_a_good_bot_citizen_of_reddit/) on reddit.
"""
for submission in reddit.redditor('ackchyually_bot').new(limit=1):
		comment = submission.id
		print ("First Comment Grabbed! ID: " + comment)
while(1>0):
	time.sleep(5)
	print ("Refreshing...")
	for submission in reddit.redditor('ackchyually_bot').new(limit=1):
		lastpost = submission.id
		print ("Last Post Found! ID: " + lastpost)
	if (comment != lastpost):
		print("New post found! Replying...")
		try:
			submission.reply(reply)
			comment = submission.id
			print("Replied. Goodnight ⭐")
		except:
			print("Uh-oh, something went wrong.")
		time.sleep(60)
