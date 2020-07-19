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
    def setupenv(self):
        return praw.Reddit(client_id = os.getenv('REDDIT_ID'),client_secret=os.getenv('REDDIT_KEY'),user_agent = 'covidhelpbotscript', username = 'Cautious_Research_23', password = os.getenv('REDDIT_PASSWORD'))
    def findhot(self,subreddit,posts=1):
        reddit = self.setupenv()
        hot_posts = reddit.subreddit(subreddit)
        hot_posts = hot_posts.hot(limit=posts)
        return hot_posts
    def linkpost(self,subreddit,id):
        return "https://www.reddit.com/r/"+str(subreddit)+"/comments/"+str(id)
    @commands.command()
    async def reddit(self,ctx,subreddit,posts=1):
        hot_posts = self.findhot(subreddit,posts)
        for id in hot_posts:
            await ctx.send(self.linkpost(subreddit,id))
def setup(bot):
    bot.add_cog(reddit(bot))