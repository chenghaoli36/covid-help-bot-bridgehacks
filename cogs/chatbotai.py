# chatbotai.py

# used for dialogflow api implementation. edited version of discord.py diaflow template https://github.com/SpectrixOfficial/discordpy-dialogflow-chatbot/blob/master/async/chatbot-ext.py

import json, apiai, discord, asyncio, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

ai = apiai.ApiAI(os.getenv("DIALOGFLOW_KEY"))
class chat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self,message):
        if(not message.author.bot and self.bot.user in message.mentions):
            try:
                if message.content.startswith(("$", "!", "?", "-", "*", "`", "~", "+", "/", ";", "=", "&", ">")):
                    pass
                else:
                    async with message.channel.typing():
                        user_message = message.content.replace(message.guild.me.mention,'') if message.guild else message.content
                        request = ai.text_request()
                        request.query = user_message
                        response = json.loads(request.getresponse().read())
                        result = response['result']
                        action = result.get('action')
                    print(response)
                    await message.channel.send(f"{message.author.mention} {response['result']['fulfillment']['speech']}")
            except Exception as error:
                await message.channel.send("Make sure you didn't give too much or too little input and try agian.")
                print(error)
def setup(bot):
    bot.add_cog(chat(bot))