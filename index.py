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


@client.event
async def on_message(message):
    allowed_channels = ["wholesome", "memes-jokes", "goodboy"]
    if message.channel.name in allowed_channels:
        if message.author == client.user:
            return

        if message.content == "doggo?":
            await message.add_reaction("🐶")
            await message.channel.send("woof woof!")
        elif message.content == "hi goodboy":
            await message.add_reaction("💛")
            await message.channel.send(embed=introEmbed)
        elif message.content == "goodboy help":
            await message.add_reaction("🤝")
            await message.channel.send(embed=helpEmbed)
        else:
            score, emotion = getEmotion(message.content)

            if score >= 0.85 and random.uniform(0, 1) >= 0.50:
                # with open("./classes.json", "r") as f:
                #     classes = json.load(f)
                #     link = random.choice(classes[emotion])

                idx = random.randint(1, len(os.listdir(f"./images/{emotion}")))
                paths = [
                    f"./images/{emotion}/{emotion}-{idx}.png",
                    f"./images/{emotion}/{emotion}-{idx}.gif",
                ]
                for path in paths:
                    if os.path.isfile(path):
                        await message.reply(
                            file=discord.File(path), mention_author=False
                        )
                        break


from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client.run(DISCORD_TOKEN)
