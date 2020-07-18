import json, apiai, discord, asyncio
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
class chat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self,message):
        if(message.author == discord.Client().user):
            return
def setup(bot):
    bot.add_cog(chat(bot))