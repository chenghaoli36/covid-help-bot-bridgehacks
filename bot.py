# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/.')

client = discord.Client()

@bot.event
async def on_ready():
    print("its up")

@bot.command()
async def crash(ctx):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        raise Exception("bot was commanded to crash")
@bot.command()
async def test(ctx):
    await ctx.send('hi')


async def on_message(message):
    if message.author == client.user:
        return
bot.run(TOKEN)