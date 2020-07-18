import discord
from discord.ext import commands
import lavalink
class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node('localhost',7000,'testing','na','music-node')
        self.bot.add_listenser(self.bot.music.voice_update_handler, 'on_socket_response')
        self.music.add_event_hook(self.track_hook)
    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id,None)
    async 
def setup(bot):
    bot.add_cog(Music(bot))