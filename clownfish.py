import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f"{client.user} is connected to Discord!")

bot = commands.Bot(command_prefix='!')


@bot.command(name='69')
async def nice(ctx):
    response = 'nice'
    await ctx.send(response)


@bot.command(name="nice_egg")
async def offer_egg(ctx):
    response = "Can I offer you a nice egg in this trying time?"
    await ctx.send(response)


@bot.command(name="dad_joke")
async def dad_joke(ctx):
    response = ""

client.run(TOKEN)
