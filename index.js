require("dotenv").config();
const { Client, Intents, MessageEmbed } = require("discord.js");

const client = new Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
    ],
});

const doggoEmbed = {
    color: 0xffd600, // Yellow
    title: "GoodBoy",
    url: "https://github.com/freyam/goodboy",
    author: {
        name: "Freyam Mehta",
        icon_url: "https://i.imgur.com/3sdcqkT.jpeg", // Me
        url: "https://github.com/freyam/",
    },
    description:
        "A discord bot that suggestively sends cute animal pictures to wholesomify the atmosphere. This bot loves to make hoomans smile :)))",
    image: {
        url: "https://i.imgur.com/X6v6dU8.jpeg", // GoodBoy Bannner Image
    },
    footer: {
        text: "Made with 💛 by Freyam!",
    },
};

client.once("ready", () => {
    console.log(`${client.user.username} on duty!`);
});

client.on("messageCreate", (msg) => {
    if (msg.content === "doggo?") {
        msg.react("😄");
        msg.channel.send("woof woof!");
    } else if (msg.content === "hi goodboy") {
        msg.react("👋");
        msg.channel.send({ embeds: [doggoEmbed] });
    }
});

client.login(process.env.DISCORD_TOKEN);
