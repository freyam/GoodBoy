import discord

introEmbed = discord.Embed(
    title="GoodBoy",
    url="https://github.com/freyam/goodboy",
    description="GoodBoy is a discord bot that contextually sends cute animal pictures to wholesomify the atmosphere.",
    color=0xFDCB58,
)
introEmbed.set_author(
    name="Freyam Mehta",
    url="https://github.com/freyam/",
    icon_url="https://i.imgur.com/3sdcqkT.jpeg",
)
introEmbed.set_image(url="https://i.imgur.com/X6v6dU8.jpeg")

helpEmbed = discord.Embed(
    title="GoodBoy's Help Desk",
    url="https://github.com/freyam/goodboy",
    description="Hi there, I am just a friendly neighbourhood doggo that sends hand-picked pictures of me and my friends reacting to the conversations happening in your server. I display 4 classes of emotions - joy, sadness, optimism, and anger.",
    color=0xFDCB58,
)
helpEmbed.set_image(url="https://i.imgur.com/X6v6dU8.jpeg")
