from asyncio import sleep

import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from random import randint

bot = commands.Bot(command_prefix="!", help_command=None)
TOKEN = open("TOKEN.txt").read()

queue = []


@bot.event
async def on_ready():
    custom = discord.Game("Do !help to get a list of available commands")
    await bot.change_presence(status=discord.Status.online, activity=custom)


@bot.command(pass_context=True)
async def random(ctx, arg):
    try:
        if int(arg) == 420:
            await ctx.send(69)
        else:
            await ctx.send(str(randint(0, int(arg))))

    except ValueError:
        await ctx.send("Only numbers are accepted")


@bot.command(pass_context=True)
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


@bot.command(pass_context=True)
async def cuicui(ctx):
    await ctx.send("Pees itself")


@bot.command(pass_context=True)
async def play(ctx, arg):
    try:
        voice = get(bot.voice_clients, guild=ctx.guild)

        if not queue:
            queue.append(arg)
            await ctx.send("Song added to queue")
            channel = ctx.author.voice.channel
            await channel.connect()

        if not voice.is_playing():
            while queue:
                ybdl_options = {'format': 'bestaudio', 'noplaylist': 'True'}
                ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                await ctx.send("Playing song")
                with YoutubeDL(ybdl_options) as ydl:
                    info = ydl.extract_info(queue[0], download=False)
                url = info['formats'][0]['url']
                voice.play(FFmpegPCMAudio(url, **ffmpeg_options))
                voice.is_playing()
                while voice.is_playing():
                    await sleep(1)
                queue.pop(0)
            await voice.disconnect()

        else:
            queue.append(arg)
            for i in range(len(queue)):
                await ctx.send(queue[i])
            return

    except AttributeError:
        await ctx.send("You are not in a voice channel")


@bot.command(pass_context=True)
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    await voice.disconnect()
    queue.clear()


@bot.command(pass_context=True)
async def skip(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if queue[0]:
        await ctx.send("Skipping song")
        ybdl_options = {'format': 'bestaudio', 'noplaylist': 'True'}
        ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice.stop()
        with YoutubeDL(ybdl_options) as ydl:
            info = ydl.extract_info(queue[0], download=False)
        url = info['formats'][0]['url']
        voice.play(FFmpegPCMAudio(url, **ffmpeg_options))
    else:
        await ctx.send("Nothing to skip")

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.set_author(name="CuiBot's Help")
    embed.add_field(name="!random", value="Returns a random number between 0 and stated number.", inline=False)
    embed.add_field(name="!roll", value="Rolls a desired dice type (d4, d6, d8, d10, d12, d20 and d100).", inline=False)
    embed.add_field(name="!cuicui", value="Such a dirty guinea pig.", inline=False)
    embed.add_field(name="!play", value="Plays audio from URL, if currently playing adds audio tu queue.", inline=False)
    embed.add_field(name="!stop", value="Disconnects bot from channel, clears queue and stops playing audio.", inline=False)
    embed.add_field(name="!skip", value="Skips current song.", inline=False)

    await author.send(embed=embed)


bot.run(TOKEN)
