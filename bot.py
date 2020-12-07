import os
# import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

default_prefix = '!'
bot = commands.Bot(command_prefix=default_prefix)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong!')


bot.run(TOKEN)
