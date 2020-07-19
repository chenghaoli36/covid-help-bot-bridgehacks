# news.py

# suposed to be a thing that can post news

import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands
from redditenv import *
import os.path
import sys
load_dotenv()
class news(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def broadcast(self,ctx, *,msg):
        if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
            for server in self.bot.guilds:
                await server.text_channels[0].send(msg)
    @commands.command()
    async def news(self,ctx):
        post = findhot("news")
        for id in post:
            await ctx.send(linkpost("news",id))
    @commands.command()
    async def covidnews(self,ctx):
        post = findhot("coronavirus",2)
        for id in post:
            await ctx.send(linkpost("coronavirus",id))
def setup(bot):
    bot.add_cog(news(bot))