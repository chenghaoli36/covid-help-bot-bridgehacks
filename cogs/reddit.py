# ping.py

# used for reddit browing and news posting

# reddit.py

#reddit api to browse reddit while on bot. used as source of info ig

import discord
import praw
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()

class reddit(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def hotonreddit(self,ctx,subreddit):
        reddit = praw.Reddit(client_id = '4JkADmoHNdaAKg',client_secret=os.getenv('REDDIT_KEY'))
        hot_post = reddit.subreddit(subreddit)
        hot_post = hot_post.hot(limit=1)
        for i in hot_post:
            print(i)
def setup(bot):
    bot.add_cog(reddit(bot))