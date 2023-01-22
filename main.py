from discord.ext import commands
from discord.ext import tasks
import discord
import sys

token = sys.argv[1]
prefix = sys.argv[2]

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print('-' * 20)
    print('Logged in as')
    print(f'User: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'Token: {token}')
    print('-' * 20)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(token)
