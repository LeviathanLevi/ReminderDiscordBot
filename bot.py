import os
import asyncio
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

client = commands.Bot(command_prefix='', self_bot=True)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TARGET_USER_ID = os.getenv('USER_TARGET_ID')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

async def getUser(TARGET_USER_ID):
    await client.wait_until_ready()
    user = None
    if user == None:
        user = await client.fetch_user(TARGET_USER_ID)
        print('Target User:',user)

    return


client.loop.create_task(getUser(TARGET_USER_ID))

client.run(TOKEN)

#await user.send("Hello")
#print('message sent')