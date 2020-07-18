# ping.py

# probably the least useful thing in the bot but fun to have
# also serves as a template for other cogs ima write

import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong! "+str(round(self.client.latency*1000))+"ms")

def setup(client):
    client.add_cog(Ping(client))