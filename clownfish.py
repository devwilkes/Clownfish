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
    """ Automatically detects '69' in user messages and replies with 'nice'.
    """
    response = 'nice'
    await ctx.send(response)
    
@bot.command(name="smack")
async def smack(ctx):
    """ Allows a user to smack another user across the face (virtually).

    Args:
        ctx (_type_): _description_
    """
    


@bot.command(name="nice_egg")
async def offer_egg(ctx):
    """ Offers the user an image of an egg.
    It's Always Sunny In Philadelphia reference.

    Args:
        ctx (_type_): _description_
    """
    response = "Can I offer you a nice egg in this trying time?"
    await ctx.send(response)


@bot.command(name="dad_joke")
async def dad_joke(ctx):
    """ Tells the user a corny dad joke.

    Args:
        ctx (_type_): _description_
    """
    response = ""

client.run(TOKEN)
