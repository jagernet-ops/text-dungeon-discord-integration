# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

actions = ["!play", "!message"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if(message.content == actions[0]):
        await message.channel.send()
    elif(message.content == actions[1]):
        await message.channel.send()
    

client.run(TOKEN)
