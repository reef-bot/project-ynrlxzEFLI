# filter_commands.py

import discord
from discord.ext import commands
from ..utils.logging import log_moderation_action

class FilterCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Check for profanity
        profanity_list = ["profanity1", "profanity2", "profanity3"]
        if any(word in message.content for word in profanity_list):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using profanity.")
            await log_moderation_action(message.guild, f"{message.author} was warned for using profanity.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Check for spam
        spam_threshold = 5
        if len(message.content) > spam_threshold:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please avoid spamming.")
            await log_moderation_action(message.guild, f"{message.author} was warned for spamming.")

def setup(bot):
    bot.add_cog(FilterCommands(bot))