import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.command()
    async def clear(self, ctx,amount=10):
        await ctx.channel.purge(limit = amount+1)
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send("Member kicked:"+member.mention)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send("Member banned:"+member.mention)
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name,member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator)==(member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send("Member unbanned:"+user.mention)
                return

def setup(client):
    client.add_cog(Moderation(client))