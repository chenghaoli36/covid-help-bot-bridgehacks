# ping.py

# used for reddit browing and news posting

import discord
import praw
from discord.ext import commands
from dotenv import load_dotenv
import os
import urllib.request as req
import time
from pprint import pprint
import authenticate
load_dotenv()

reddit = autheticate.redditAuthenticate(os.getenv('PREFIX'))

class reddit(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    

def setup(bot):
    bot.add_cog(reddit(bot))