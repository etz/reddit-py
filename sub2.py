#!/usr/bin/python
import praw
import time
import random

client = ""
secret = ""
user = ""
password = ""
agent = "Sub4SubAgent"

title = ['Legit YT Sub4Sub & Watchtime Trade', 'SUB4SUB, View4View, Fast and easy', 'Sub4Sub & Watchtime Boost']
links = ["https://www.youtube.com/watch?v=hQc3Y4axOAI","https://www.youtube.com/watch?v=bdAQibsH8s4","https://www.youtube.com/watch?v=FxV9PWqj7Mg","https://www.youtube.com/watch?v=lUGOdHMPstE","https://www.youtube.com/watch?v=7YeUiN1cGaQ","https://www.youtube.com/watch?v=IFBYQyRGWj8","https://www.youtube.com/watch?v=BVAFAWCMFxw","https://www.youtube.com/watch?v=L5iPi5-o4Dc","https://www.youtube.com/watch?v=DMCXD7v5Z3A","https://www.youtube.com/watch?v=rownm8UVlUk","https://www.youtube.com/watch?v=Hmmc5qV-VG0","https://www.youtube.com/watch?v=Knst9wEuoBY","https://www.youtube.com/watch?v=6OdufE1bUk8","https://www.youtube.com/watch?v=N7DXKHh76LA","https://www.youtube.com/watch?v=2A__JfXPyMM","https://www.youtube.com/watch?v=VcERnoDGudE","https://www.youtube.com/watch?v=OBsPg_y3HXY","https://www.youtube.com/watch?v=DYUrPjhwcq8","https://www.youtube.com/watch?v=I3us0qIfTNE","https://www.youtube.com/watch?v=dITAgXl5qFY","https://www.youtube.com/watch?v=Iugn34FSIxo","https://www.youtube.com/watch?v=cA_jAOF3tG4","https://www.youtube.com/watch?v=EIrGA17LL2Y","https://www.youtube.com/watch?v=2Q9cGPkDpvc","https://www.youtube.com/watch?v=HH2LvFj1-Bo","https://www.youtube.com/watch?v=HKdDk_K43iI","https://www.youtube.com/watch?v=adOQ-Pqz9Z0","https://www.youtube.com/watch?v=R-6IS5nBXQ8","https://www.youtube.com/watch?v=YJkYg2GdsC0","https://www.youtube.com/watch?v=RZLyeyk3uk0"]
reddit = praw.Reddit(client_id=client, client_secret=secret, password=password, user_agent=agent, username=user)

counter = 0
messaged = []
remessaged = []
start_time = unix.time()
submissionList = []

while(1>0):
    if (time.time() > (start_time + 86400)):
        start_time = time.time()
        remessaged = messaged
        messaged = []
    if (counter == 0):
        post = '#Subscribe: [My YouTube](' + random.choice(links) + '). \n\n 1. Watch at least 60 seconds before subscribing. \n\n 2. Upvote this post for visibility! \n\n 3. Reply below with your video or channel URL. \n I will subscribe and leave a comment on your video! \n\n I also am willing to watch your playlists in exchange for mine, just let me know by posting below!'
        print ("Posting thread")
        reddit.subreddit('Sub4Sub').submit(random.choice(title), selftext=post)
        counter = 23
    for submission in reddit.subreddit('Sub4Sub').new(limit=12):
        print ("Reading new submission")
        time.sleep(3) #3
        #print (submission.author)
        submissionList.append(submission.author)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            print ("Reading comment authors")
            print (comment.author)
            submissionList.append(comment.author)
    for user in submissionList:
        #print (user)
        if user in messaged:
            print ("Already messaged " + str(user) + " today, ignoring!")
            submissionList.remove(user)
            continue
        if user in remessaged:
            pmessage = 'hey again, I saw that you posted looking for subs once again. I have already subscribed to your channel and was hoping you could return the favor if you have not yet!\n\n #[My channel linked here](' + random.choice(link) + ') \n\n Im also looking for more watchtime if you are too, just [play this playlist](https://www.youtube.com/watch?v=HiJRQrgclvs&list=PLiaqnw9VgH2-sVwyGaaz_kY3gylL7JFeD) on mute in the background and reply with your own playlist. Thanks =)'
            print ("Messaged " + str(user) + " yesterday, sending playlist!")
            reddit.redditor(str(user)).message('Sub4Sub/Watchtime', pmessage)
            print ("Successfully sent " + str(user) + " a message!")
            messaged.append(user)
            submissionList.remove(user)
            continue
        try:
            pmessage = 'Hi there, I saw that you posted in r/Sub4sub recently. I have subscribed to your channel and was hoping you could return the favor!\n\n #[My channel linked here](' + random.choice(link) + ') \n\n If you are interested in trading watch time, then [play this playlist](https://www.youtube.com/watch?v=HiJRQrgclvs&list=PLiaqnw9VgH2-sVwyGaaz_kY3gylL7JFeD) on mute in the background and send your own playlist. Thanks =)'
            reddit.redditor(str(user)).message('Sub4Sub/Watchtime', pmessage)
            print ("Successfully sent " + str(user) + " a message!")
            messaged.append(user)
            submissionList.remove(user)
            print ("Sleeping to avoid the reddit monster!")
            time.sleep(10) #6
        except:
            print ("Ran into an error!")
            continue
    print("~ Shutting down for 20 minutes ~")
    time.sleep(1200) #1200
    counter = counter - 1
