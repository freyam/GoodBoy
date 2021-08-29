import os
import discord
import random
import json

from emotions import *
from embed import *

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user.name} on duty! woof woof!")


allowed_channels = []


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == "goodboy?":
        await message.add_reaction("🐶")
        await message.channel.send("woof woof!")
    elif message.content == "hi goodboy":
        await message.add_reaction("💛")
        await message.channel.send(embed=introEmbed)
    elif message.content == "goodboy help":
        await message.add_reaction("🤝")
        await message.channel.send(embed=helpEmbed)
    elif message.content == "goodboy go sleep":
        allowed_channels.remove(message.channel.name)
        await message.add_reaction("💤")
        await message.channel.send("see you soon!")
    elif message.content == "goodboy wake up":
        allowed_channels.append(message.channel.name)
        await message.add_reaction("🌤️")
        await message.channel.send("rise and shine!")
    elif message.content == "goodboy go fetch":
        await message.add_reaction("🥎")
        await message.reply("https://imgur.com/annKRYx", mention_author=True)
    elif message.channel.name in allowed_channels:
        score, emotion = getEmotion(message.content)
        if score >= 0.875 and random.uniform(0, 1) > 0.5:
            with open("./classes.json", "r") as f:
                classes = json.load(f)
                link = random.choice(classes[emotion])
                await message.reply(link, mention_author=False)


from dotenv import load_dotenv

load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))
