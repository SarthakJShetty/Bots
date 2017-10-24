import praw
import os
import re
import pdb

reddit=praw.Reddit('bot1')

#Lels check if the file exists or not
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to=[]
else:
	with open("posts_replied_to.txt","r") as f:
		posts_replied_to=f.read()
		posts_replied_to=posts_replied_to.split("\n")
		posts_replied_to=list(filter(None,posts_replied_to))
 
#Lels go the subreddit now
subreddit=reddit.subreddit('pythonforengineers')

#Lels check the top five posts in the sub
for submission in subreddit.hot(limit=10):
	if submission.id not in posts_replied_to:
		if re.search("i love python",submission.title,re.IGNORECASE):
			submission.reply("Botty bot says: Me too!")
			print("Bot has replied to:", submission.title)
			posts_replied_to=posts_replied_to.append(submission.id)

#Lels add the submission ID to the list now and
with open("posts_replied_to.txt","w ") as f:
	for post_id in posts_replied_to:
		f.write(post_id+"\n")