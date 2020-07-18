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
        bot.load_extension("cogs."+str(extension))

@bot.command()
async def unload(ctx, extension):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        bot.unload_extension("cogs."+str(extension))

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension("cogs."+str(filename[:-3]))

@bot.command()
async def crash(ctx):
    if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
        raise Exception("crash command",ctx.author.id)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! "+str(round(bot.latency*1000))+"ms")

@bot.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit = amount+1)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send("Member kicked:"+member.mention)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send("Member banned:"+member.mention)

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name,member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("Member unbanned:"+user.mention)
            return

bot.run(TOKEN)