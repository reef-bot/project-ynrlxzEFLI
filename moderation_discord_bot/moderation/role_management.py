# role_management.py

import discord
from discord.ext import commands

from ..utils.database import Database

class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command(name='add_role')
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"{member.mention} has been given the {role.name} role.")
            
            # Log the action
            self.db.log_moderation_action(ctx.guild.id, ctx.author.id, f"Added {role.name} role to {member.name}")
            
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='remove_role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} no longer has the {role.name} role.")
            
            # Log the action
            self.db.log_moderation_action(ctx.guild.id, ctx.author.id, f"Removed {role.name} role from {member.name}")
            
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='list_roles')
    async def list_roles(self, ctx, member: discord.Member):
        roles = member.roles
        role_names = [role.name for role in roles if role.name != '@everyone']
        await ctx.send(f"{member.name} has the following roles: {', '.join(role_names)}")

def setup(bot):
    bot.add_cog(RoleManagement(bot))