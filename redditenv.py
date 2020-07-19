# redditenv.py

#reddit api to browse reddit while on bot. used as source of info ig

import discord
import praw
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os.path
import sys
def setupenv():
    return praw.Reddit(client_id = os.getenv('REDDIT_ID'),client_secret=os.getenv('REDDIT_KEY'),user_agent = 'covidhelpbotscript', username = 'Cautious_Research_23', password = os.getenv('REDDIT_PASSWORD'))
def findhot(subreddit,posts=1):
    reddit = setupenv()
    hot_posts = reddit.subreddit(subreddit)
    hot_posts = hot_posts.hot(limit=posts)
    return hot_posts
def linkpost(subreddit,id):
    return "https://www.reddit.com/r/"+str(subreddit)+"/comments/"+str(id)