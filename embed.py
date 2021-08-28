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
helpEmbed.add_field(
    name="Dog Whistle",
    value="""
    - `goodboy?` to check if GoodBoy is awake and healthy.
    - `hi goodboy` to show GoodBoy's information card.
    - `goodboy help` to see this card.
    - `goodboy go sleep` to let GoodBoy rest.
    - `goodboy wake up` to wake GoodBoy up.
    - `goodboy go fetch` to play fetch with GoodBoy.

    GoodBoy also replies to all the messages by understanding the emotion of the message and reacting to them by sending a picture of his friends.
    """,
)
