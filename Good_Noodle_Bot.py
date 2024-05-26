import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
load_dotenv()

description = 'Good Noodle Star bot.'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event()
async def on_ready():
    print('Log in.')
    print(f'User: {bot.user}')
    print(f'ID: {bot.user.id}')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(os.getenv("DISCORD_TOKEN"))