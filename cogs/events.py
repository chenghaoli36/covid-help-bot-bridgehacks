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
        if message.author == discord.Client().user:
            return
def setup(client):
    client.add_cog(Events(client))