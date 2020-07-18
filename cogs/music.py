# music.py

# uses lavalink stuff
# github example repo for lavalink here:https://github.com/Devoxin/Lavalink.py/blob/master/examples/music.py
# cool music bot stuff here:

import re
import discord
from discord.ext import commands
import lavalink
from discord import utils
url_rx = re.compile(r'https?://(?:www\.)?.+')
class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot.lavalink = lavalink.Client(bot.user.id)
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node('localhost', 8888,'testing','na','music-node')
        self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(error.original)
    def cog_unload(self):
        self.bot.lavalink._event_hooks.clear()
    @commands.command(name = 'joinvc')
    async def joinvc(self,ctx):
        member = utils.find(lambda m: m.id == ctx.author.id, ctx.guild.members)
        if member is not None and member.voice is not None:
            vc = member.voice.channel
            player = self.bot.music.player_manager.create(ctx.guild.id, endpoint = str(ctx.guild.region))
            if not player.is_connected:
                player.store('channel',ctx.channel.id)
                await self.connect_to(ctx.guild.id, str(vc.id))
                await ctx.send('Connected.')
    @commands.command(name = "leavevc")
    async def leavevc(self,ctx):
        try:
            player = self.bot.music.player_manager.get(ctx.guild.id)
            if not player.is_connected:
                return await ctx.send('Not connected.')
            if not ctx.author.voice or (player.is_connected and ctx.author.voice.channel.id != int(player.channel_id)):
                return await ctx.send('You\'re not in my voicechannel!')
            player.queue.clear()
            await player.stop()
            await self.connect_to(ctx.guild.id, None)
            await ctx.send('Disconnected.')
        except:
            await ctx.send('Error! try using the joinvc and then leavevc command again.')
    @commands.command(name = 'search')
    async def search(self,ctx, *, query: str):
        try:
            player = self.bot.music.player_manager.get(ctx.guild.id)
            query = query.strip('<>')
            query = 'ytsearch:'+query
            results = await player.node.get_tracks(query)
            if not results or not results['tracks']:
                return await ctx.send('Nothing found!')
            tracks = results['tracks'][0:10]
            i=0
            query_result = ''
            for track in tracks:
                i=i+1
                query_result = query_result + f'{i}) {track["info"]["title"]} - {track["info"]["uri"]}\n'
            embed = discord.Embed(color = discord.Color.blurple())
            embed.description = query_result
            embed.title = "querey results:"
            await ctx.channel.send(embed=embed)
            def check(m):
                return m.author.id == ctx.author.id
            response = await self.bot.wait_for('message',check = check)
            track = results['tracks'][int(response.content)-1]
            track = lavalink.models.AudioTrack(track, ctx.author.id, recommended=True)
            player.add(requester = ctx.author.id,track=track)
            await ctx.channel.send("Added to queue")
            if not player.is_playing:
                await player.play()
        except Exception as error:
            await ctx.channel.send("There was an error, please try again.(maybe run joinvc command one more time)")
            print(error)
    @commands.command(name = 'play')
    async def play(self,ctx, *, query):
        try:
            player = self.bot.music.player_manager.get(ctx.guild.id)
            query = query.strip('<>')
            if not url_rx.match(query):
                query = f'ytsearch:{query}'
            results = await player.node.get_tracks(query)
            if not results or not results['tracks']:
                return await ctx.send('Nothing found!')
            embed = discord.Embed(color=discord.Color.blurple())
            if results['loadType'] == 'PLAYLIST_LOADED':
                tracks = results['tracks']
                for track in tracks:
                    player.add(requester=ctx.author.id, track=track)
                embed.title = 'Playlist queued!'
                embed.description = f'{results["playlistInfo"]["name"]} - {len(tracks)} tracks'
            else:
                track = results['tracks'][0]
                embed.title = 'Track queued'
                embed.description = f'[{track["info"]["title"]}]({track["info"]["uri"]})'
                track = lavalink.models.AudioTrack(track, ctx.author.id, recommended=True)
                player.add(requester=ctx.author.id, track=track)
            await ctx.send(embed=embed)
            if not player.is_playing:
                await player.play()
        except Exception as error:
            await ctx.channel.send("There was an error, please try again.(maybe run joinvc command agin)")
            print(error)
    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id,None)
    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)
def setup(bot):
    bot.add_cog(Music(bot))