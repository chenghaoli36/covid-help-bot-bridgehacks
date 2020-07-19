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

class Coronavirus(commands.Cog):
    def __init__(self,bot):
        self.driver = webdriver.Chrome()
        self.bot = bot
    @commands.command()
    async def coviddata(self,ctx):
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(., 'USA')]")
        row = country_element.find_element_by_xpath("./..")
        print(row.text)
        data = row.text.split(" ")
        total_cases = data[2]
        new_cases = data[3]
        total_deaths = data[4]
        new_deaths = data[5]
        active_cases = data[6]
        total_recovered = data[7]
        serious_critical = data[8]
        embed = discord.Embed(color = discord.Color.blurple())
        embed.description = "Country: " + country_element.text+"\n"+"Total cases: " + total_cases+"\n"+"New cases: " + new_cases+"\n"+"Total deaths: " + total_deaths+"\n"+"New deaths: " + new_deaths+"\n"+"Active cases: " + active_cases+"\n"+"Total recovered: " + total_recovered+"\n"+"Serious, critical cases: " + serious_critical+"\n"
        embed.title = "results:"
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Coronavirus(bot))