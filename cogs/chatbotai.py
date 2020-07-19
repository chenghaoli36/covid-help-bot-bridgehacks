# chatbotai.py

# used for dialogflow api implementation

import json, apiai, discord, asyncio, os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\code\covidhelpbot\covid-fa9e1e459d3c.json"
DIALOGFLOW_PROJECT_ID = 'covid-ltbqsu'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_APPLICATION_CREDENTIALS = 'covid-fa9e1e459d3c.json'
SESSION_ID = 'current-user-id'
class chat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self,message):
        if((not message.author.bot and self.bot.user in message.mentions) or (isinstance(message.channel, discord.channel.DMChannel) and not message.author.bot)):
            try:
                if message.content.startswith(("$", "!", "?", "-", "*", "`", "~", "+", "/", ";", "=", "&", ">")):
                    pass
                else:
                    async with message.channel.typing():
                        user_message = message.content.replace(message.guild.me.mention,'') if message.guild else message.content
                        session_client = dialogflow.SessionsClient()
                        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
                        text_input = dialogflow.types.TextInput(text=user_message, language_code=DIALOGFLOW_LANGUAGE_CODE)
                        query_input = dialogflow.types.QueryInput(text=text_input)
                        try:
                            response = session_client.detect_intent(session=session, query_input=query_input)
                        except InvalidArgument:
                            raise
                    print(response)
                    await message.channel.send(response.query_result.fulfillment_text)
            except Exception as error:
                await message.channel.send("Make sure you didn't give too much or too little input and try agian.")
                print(error)
def setup(bot):
    bot.add_cog(chat(bot))