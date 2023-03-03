import config
import discord
from discord.ext import commands
from HttpRequestHandler import HttpRequestHandler
import requests

http = HttpRequestHandler()

http.image("a friendly bear")
bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Online")

@bot.command()
async def text(e, *, prompt):
    await e.reply(http.text(prompt))

@bot.command()
async def image(e, *, prompt):
    await e.reply(http.image(prompt))

bot.run(config.DISCORD_TOKEN)