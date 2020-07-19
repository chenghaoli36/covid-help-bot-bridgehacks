# covid.py

# show some covid data from 'https://www.worldometers.info/coronavirus/'

import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands
from selenium import webdriver
from time import sleep
import re
from datetime import datetime
import smtplib
import os
import covidenv

class Coronavirus(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def coviddata(self,ctx,country = "USA"):
        await ctx.send("please wait while I gather the data. This may take a while(1-2 min). try again if it doesn't work")
        async with ctx.channel.typing():
            embed = discord.Embed(color = discord.Color.blurple())
            embed.description = covidenv.coviddata(country)
            embed.title = "results:"
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Coronavirus(bot))