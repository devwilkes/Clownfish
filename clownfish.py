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
    
@bot.command(name="ping")
async def hug(ctx):
    """ Allows users to check the ping response time of Clownfish.
    Args:
        ctx (_type_): _description_
    """
    response = f"Pong! \n Response time: " + "seconds."
    

@bot.command(name="hug")
async def hug(ctx):
    """ Allows a user to virtually hug another user or receive a virtual hug from the bot.

    Args:
        ctx (_type_): _description_
    """
    
@bot.command(name="smack")
async def smack(ctx):
    """ Allows a user to smack another user across the face (virtually).

    Args:
        ctx (_type_): _description_
    """
    
@bot.command(name="birthday")
async def birthday(ctx):
    """ If the user types any message in the server, and it is their birthday, CLownfish will detect it, 
    and throw a surprise birthday party for them.

    Args:
        ctx (_type_): _description_
    """
    response = "Happy Birthday!"
    
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

@bot.command(name="cat_meme")
async def cat_meme(ctx):
    """ Generates a random cat meme.

    Args:
        ctx (_type_): _description_
    """
    response = ""
    
@bot.command(name="cat_meme_retro")
async def cat_meme_retro(ctx):
    """ Generates a random old-Internet cat meme.

    Args:
        ctx (_type_): _description_
    """
    response = ""
    
client.run(TOKEN)
