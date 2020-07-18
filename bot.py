# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=os.getenv('PREFIX'))

@bot.command()
async def load(ctx, extension):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        try:
            bot.load_extension("cogs."+str(extension))
            await ctx.send("Done! "+ctx.author.mention)
        except Exception as error:
            print(error)
            await ctx.send("loading failed")

@bot.command()
async def unload(ctx, extension):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        try:
            bot.unload_extension("cogs."+str(extension))
            await ctx.send("Done! "+ctx.author.mention)
        except Exception as error:
            print(error)
            await ctx.send("unloading failed")

@bot.command()
async def reload(ctx, extension):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        try:
            bot.unload_extension("cogs."+str(extension))
            bot.load_extension("cogs."+str(extension))
            await ctx.send("Done! "+ctx.author.mention)
        except Exception as error:
            print(error)
            await ctx.send("reload failed")

@bot.command()
async def reloadall(ctx):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        try:
            for filename in os.listdir('./cogs'):
                if filename.endswith(".py"):
                    bot.unload_extension("cogs."+str(filename[:-3]))
                    bot.load_extension("cogs."+str(filename[:-3]))
            await ctx.send("Done! "+ctx.author.mention)
        except Exception as error:
            print(error)
            await ctx.send("reload failed")

@bot.event
async def on_ready():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            bot.load_extension("cogs."+str(filename[:-3]))

bot.run(TOKEN)