import discord
import requests
from discord.ext import commands
from random import randint
client = commands.Bot(command_prefix="!")

@client.command()
async def random(ctx, arg):
    try:

        await ctx.send(str(randint(0, int(arg))))

    except:

        await ctx.send("Only numbers are accepted")


client.run("ODkwMzYwMzM1NjgzNDI0MjU3.YUuqrg.Q68KMXR_iWESOBC9LdTLYlvQiJA")