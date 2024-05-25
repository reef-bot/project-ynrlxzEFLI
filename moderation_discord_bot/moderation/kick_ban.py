# File: kick_ban.py

import discord
from discord.ext import commands

from utils.logging import log_moderation_action

class KickBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='Kicks a user from the server')
    async def kick_user(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked from the server.')
            await log_moderation_action(ctx.guild, f'Kicked {member} - Reason: {reason}', ctx.author)
        else:
            await ctx.send('You do not have permission to kick members.')

    @commands.command(name='ban', help='Bans a user from the server')
    async def ban_user(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned from the server.')
            await log_moderation_action(ctx.guild, f'Banned {member} - Reason: {reason}', ctx.author)
        else:
            await ctx.send('You do not have permission to ban members.')

def setup(bot):
    bot.add_cog(KickBan(bot))