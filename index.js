require("dotenv").config();
const { Client, Intents } = require("discord.js");

const classes = require("./classes.json");
const getSentiment = require("./sentiment.js");
const { introEmbed, helpEmbed } = require("./embed.js");

const client = new Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
    ],
});

client.once("ready", () => {
    console.log(`${client.user.username} on duty!`);
});

client.on("messageCreate", (msg) => {
    const message = msg.content;
    const channel = msg.channel;
    const author = msg.author;

    if (message === "doggo?") {
        msg.react("😄");
        channel.send("woof woof!");
    } else if (message === "hi goodboy") {
        msg.react("💛");
        channel.send({ embeds: [introEmbed] });
    } else if (message === "goodboy help") {
        msg.react("🤝");
        channel.send({ embeds: [helpEmbed] });
    } else if (message === "x" && !author.bot) {
        const sentiment = getSentiment(message);
        const randomIndex = Math.floor(
            Math.random() * classes[sentiment].length
        );
        const reaction = classes[sentiment][randomIndex];
        channel.send(reaction);
    }
});

client.login(process.env.DISCORD_TOKEN);
