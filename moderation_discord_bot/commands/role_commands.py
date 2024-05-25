# role_commands.py

import discord
from discord.ext import commands

class RoleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add_role')
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"Added {role.name} role to {member.display_name}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='remove_role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"Removed {role.name} role from {member.display_name}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

def setup(bot):
    bot.add_cog(RoleCommands(bot))