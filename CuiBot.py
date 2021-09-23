import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Se mea")
client.run("ODkwMzYwMzM1NjgzNDI0MjU3.YUuqrg.Q68KMXR_iWESOBC9LdTLYlvQiJA")
