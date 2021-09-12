# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild)

# when someone posts in a quote channel log the quote, parse it, increment score for user tagged

# when someone types "quote unclaimed" bot should post a list of top 50 names that are not claimed

# when someone types "quote iclaim [tag]" bot should link user to this tag

# when someone types "quote scoreboard" bot should list the top 5 tags and their scores

client.run(TOKEN)