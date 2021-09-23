import discord
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix="!", help_command=None)
TOKEN = "ODkwMzYwMzM1NjgzNDI0MjU3.YUuqrg.Q68KMXR_iWESOBC9LdTLYlvQiJA"

@bot.event
async def on_ready():
    custom = discord.Game("Do !help to get a lis of available commands")
    await bot.change_presence(status=discord.Status.online, activity=custom)


@bot.command()
async def random(ctx, arg):
    try:

        await ctx.send(str(randint(0, int(arg))))

    except:

        await ctx.send("Only numbers are accepted")


@bot.command()
async def roll(ctx, arg):
    if arg.lower() == "d4":
        await ctx.send(str(randint(1, 4)))
    elif arg.lower() == "d6":
        await ctx.send(str(randint(1, 6)))
    elif arg.lower() == "d8":
        await ctx.send(str(randint(1, 8)))
    elif arg.lower() == "d10":
        await ctx.send(str(randint(1, 10)))
    elif arg.lower() == "d12":
        await ctx.send(str(randint(1, 12)))
    elif arg.lower() == "d20":
        await ctx.send(str(randint(1, 20)))
    elif arg.lower() == "d100":
        await ctx.send(str(randint(1, 100)))
    else:
        await ctx.send("Incorrect dice type please use d4, d6, d8, d10, d12, d20 or d100")


@bot.command()
async def cuicui(ctx):
    await ctx.send("Pees itself")

@bot.command()
async def play(ctx, arg):
    channel = ctx.author.voice.channel
    await channel.connect()

    server = ctx.message.guild
    voiceClient =  bot.voice_clients(server)


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.set_author(name="CuiBot's Help")
    embed.add_field(name="!random", value="Returns a random number between 0 and stated number", inline=False)
    embed.add_field(name="!roll", value="Rolls a desired dice type (d4, d6, d8, d10, d12, d20 and d100)", inline=False)
    embed.add_field(name="!cuicui", value="Sucha dirtty guinea pig", inline=False)

    await author.send(embed=embed)


bot.run(TOKEN)
