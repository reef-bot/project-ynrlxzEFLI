# user_commands.py

import discord
from discord.ext import commands
from utils.logging import log_moderation_action

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    async def kick_member(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked.')
            log_moderation_action(ctx.guild, ctx.author, member, 'kick', reason)
        else:
            await ctx.send("You don't have permission to kick members.")

    @commands.command(name='ban')
    async def ban_member(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned.')
            log_moderation_action(ctx.guild, ctx.author, member, 'ban', reason)
        else:
            await ctx.send("You don't have permission to ban members.")

def setup(bot):
    bot.add_cog(UserCommands(bot))