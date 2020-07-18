# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

client = discord.Client()

@bot.event
async def on_ready():
    print("bot ready")

async def on_message(message):
    if message.author == client.user:
        return

@bot.command()
async def load(ctx, extension):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        try:
            bot.load_extension("cogs."+str(extension))
            await ctx.send("Done! "+ctx.author.mention)
        except:
            await ctx.send("loading failed")

@bot.command()
async def unload(ctx, extension):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        try:
            bot.unload_extension("cogs."+str(extension))
            await ctx.send("Done! "+ctx.author.mention)
        except:
            await ctx.send("unloading failed")

@bot.command()
async def reload(ctx, extension):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        try:
            bot.unload_extension("cogs."+str(extension))
            bot.load_extension("cogs."+str(extension))
            await ctx.send("Done! "+ctx.author.mention)
        except:
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
        except:
            await ctx.send("reload failed")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension("cogs."+str(filename[:-3]))

bot.run(TOKEN)