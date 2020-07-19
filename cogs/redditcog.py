# redditcog.py

# used for reddit browing and news posting


import discord
from discord.ext import commands
import os.path
import sys
from redditenv import *
class redditcog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def reddit(self,ctx,subreddit,posts=1):
        hot_posts = findhot(subreddit,posts)
        for id in hot_posts:
            await ctx.send(linkpost(subreddit,id))
def setup(bot):
    bot.add_cog(redditcog(bot))