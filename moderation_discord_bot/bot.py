# bot.py

import discord
from discord.ext import commands
from commands import filter_commands, moderation_commands, role_commands, user_commands
from utils import config, database, logging
from moderation import filtering, role_management, kick_ban, custom_settings

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Add commands from different command files
bot.add_cog(filter_commands.FilterCommands(bot))
bot.add_cog(moderation_commands.ModerationCommands(bot))
bot.add_cog(role_commands.RoleCommands(bot))
bot.add_cog(user_commands.UserCommands(bot))

# Run the bot
bot.run(config.TOKEN)