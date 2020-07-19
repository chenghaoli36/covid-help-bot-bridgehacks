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
    async def reddit(self,ctx,subreddit,posts=1):
        reddit = praw.Reddit(client_id = os.getenv('REDDIT_ID'),client_secret=os.getenv('REDDIT_KEY'),user_agent = 'covidhelpbotscript', username = 'Cautious_Research_23', password = os.getenv('REDDIT_PASSWORD'))
        hot_post = reddit.subreddit(subreddit)
        hot_post = hot_post.hot(limit=posts)
        for i in hot_post:
            await ctx.send("https://www.reddit.com/r/"+str(subreddit)+"/comments/"+str(i))
def setup(bot):
    bot.add_cog(reddit(bot))