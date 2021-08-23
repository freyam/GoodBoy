const introEmbed = {
    color: 0xffd600, // Yellow
    title: "GoodBoy",
    url: "https://github.com/freyam/goodboy",
    author: {
        name: "Freyam Mehta",
        icon_url: "https://i.imgur.com/3sdcqkT.jpeg", // Me
        url: "https://github.com/freyam/",
    },
    description:
        "GoodBoy is a discord bot that suggestively sends cute animal pictures/gifs to wholesomify the atmosphere.",
    image: {
        url: "https://i.imgur.com/X6v6dU8.jpeg", // GoodBoy Bannner Image
    },
    footer: {
        text: "GoodBoy loves all thy hoomans!",
    },
};

const helpEmbed = {
    color: 0xffd600, // Yellow
    title: "GoodBoy Help Desk",
    url: "https://github.com/freyam/goodboy",
    author: {
        name: "Freyam Mehta",
        icon_url: "https://i.imgur.com/3sdcqkT.jpeg", // Me
        url: "https://github.com/freyam/",
    },
    description:
        "GoodBoy is a discord bot that suggestively sends cute animal pictures/gifs to wholesomify the atmosphere.",
    image: {
        url: "https://i.imgur.com/X6v6dU8.jpeg", // GoodBoy Bannner Image
    },
    fields: [
        {
            name: "**!goodboy**",
            value: "Sends a random gif/image of a cute animal.",
        },
        {
            name: "**!goodboy <animal>**",
            value: "Sends a random gif/image of a cute animal.",
        },
    ],
    footer: {
        text: "GoodBoy loves all thy hoomans!",
    },
};

module.exports = { introEmbed, helpEmbed };
