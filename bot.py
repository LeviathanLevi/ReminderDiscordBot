import os
import asyncio
import discord
import datetime
from discord.ext import commands, tasks
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='', self_bot=True)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

async def getUser(TARGET_USER_ID):
    await bot.wait_until_ready()
    user = None
    if user == None:
        user = await bot.fetch_user(TARGET_USER_ID)
        print('Target User:',user)

    return

async def startBot():
    TARGET_USER_ID = os.getenv('USER_TARGET_ID')
    await getUser(TARGET_USER_ID)
    print("here")

@tasks.loop(minutes=1)
async def updateReminders():
    timestamp = datetime.datetime.now().day
    
bot.loop.create_task(startBot())

bot.run(TOKEN)