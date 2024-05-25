# File: config.py

import os

# Discord bot token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Moderation settings
AUTOMATIC_FILTERING = True
LOGGING_ENABLED = True

# Database settings
DATABASE_NAME = 'moderation_actions.db'
DB_TABLE_NAME = 'actions'

# Discord API endpoints
DISCORD_API_URL = 'https://discord.com/api/v9'
GUILD_ENDPOINT = '/guilds/{guild_id}'
MEMBER_ENDPOINT = '/guilds/{guild_id}/members/{member_id}'
MESSAGE_ENDPOINT = '/channels/{channel_id}/messages/{message_id}'

# Customizable moderation settings
FILTER_THRESHOLD = 3
LOGGING_THRESHOLD = 5

# Role management settings
MODERATOR_ROLE = 'Moderator'
ADMIN_ROLE = 'Admin'

# Kick and ban settings
KICK_MESSAGE = 'You have been kicked from the server.'
BAN_MESSAGE = 'You have been banned from the server.'

# Filter settings
PROFANITY_FILTER = ['profanity', 'bad_word']
SPAM_FILTER = ['spam', 'link']

# Error messages
MISSING_TOKEN_ERROR = 'Discord token is missing. Please set DISCORD_TOKEN environment variable.'
DB_ERROR = 'Error connecting to the database. Please check your connection.'

# Logging messages
MODERATION_LOG = 'Moderation action logged: {}'
DB_CONNECTION_SUCCESS = 'Successfully connected to the database.'
DB_CONNECTION_CLOSE = 'Database connection closed.'