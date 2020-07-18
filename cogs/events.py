import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("bot ready")
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('prefix: '+self.client.command_prefix))
    @commands.Cog.listener()
    async def on_message(self,message):
        if(message.author == discord.Client().user):
            return
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