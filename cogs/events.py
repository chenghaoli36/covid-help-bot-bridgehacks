# events.py

# houses all the events, ex: on_ready, on_message, etc.

import discord
from discord.ext import commands
import os
class Events(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("bot ready")
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('dm/ping me to talk! prefix: '+self.client.command_prefix+". usage: "+self.client.command_prefix+"help."))
        for filename in os.listdir('./cogs'):
            if filename.endswith(".py") and filename != "events.py":
                self.client.load_extension("cogs."+str(filename[:-3]))
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send('Missing arguments! Please try again.')
        elif(isinstance(error, commands.MissingRole)):
            await ctx.send('Missing Permissions!')
        elif(isinstance(error, commands.CommandNotFound)):
            await ctx.send('Command not found!')
        else:
            print(error)
def setup(client):
    client.add_cog(Events(client))