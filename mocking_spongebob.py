import asyncio
import discord
import time
import random
import os
from datetime import datetime
from discord.ext import tasks
from discord.ext import commands
from datetime import time, timezone


bot = discord.Bot()
guildList=[1065813802425262141]

    
@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name) 
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="SHEEEEEEEESH"))
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"commands.{filename[:-3]}")

f = open("discordToken.txt", "r")
key = f.readline().strip()
f.close()
bot.run(key)