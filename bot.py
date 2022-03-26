from audioop import add
import os
import asyncio
import discord
import datetime
import reminder
from discord.ext import commands, tasks
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='', self_bot=True)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
listOfReminders = []

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

    return user

async def startBot():
    TARGET_USER_ID = os.getenv('USER_TARGET_ID')
    user = await getUser(TARGET_USER_ID)
    #hard coding reminders in for now:
    listOfReminders.append(reminder.IntervalReminder("Reminder, you should meditate!", user, 1000))

    updateReminders.start()

@tasks.loop(minutes=1)
async def updateReminders():
    #timestamp = datetime.datetime.now().day
    for reminder in listOfReminders:
        reminder.minutesRemaining -= 1
        if reminder.minutesRemaining == 0:
            await reminder.sendMessage()
            reminder.minutesRemaining = reminder.intervalInMinutes

bot.loop.create_task(startBot())

bot.run(TOKEN)