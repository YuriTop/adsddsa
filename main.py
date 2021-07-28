import discord
from discord.ext import commands
from modules.config import Config
from os import listdir

bot = commands.Bot(command_prefix='crashed.')

if __name__ == '__main__':
    bot.load_extension('cogs.crasher')

bot.run("")
