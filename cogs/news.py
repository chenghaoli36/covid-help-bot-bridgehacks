# news.py

# suposed to be a thing that can post news

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
class news(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def broadcast(self,ctx, *,msg):
        if(str(os.getenv('OWNER_ID'))==str(ctx.author.id)):
            for server in self.bot.guilds:
                await server.text_channels[0].send(msg)
def setup(bot):
    bot.add_cog(news(bot))