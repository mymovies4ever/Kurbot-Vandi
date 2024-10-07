const express = require('express');
const { Telegraf } = require('telegraf');
const fetch = require('node-fetch');

const app = express();
const bot = new Telegraf(process.env.BOT_TOKEN);

// Respond to the /start command
bot.start((ctx) => ctx.reply('Welcome! Send me a vehicle number, and I will fetch its details.'));

// Respond to vehicle registration details
bot.on('text', async (ctx) => {
    const vehicleNumber = ctx.message.text;

    // Example API call to get vehicle details (replace with actual logic)
    try {
        const vehicleData = await fetch(`https://parivahan.api/vehicle/${vehicleNumber}`);
        const data = await vehicleData.json();

        ctx.reply(`Vehicle Details:\nModel: ${data.model}\nOwner: ${data.owner}`);
    } catch (error) {
        ctx.reply('Could not fetch details for this vehicle.');
    }
});

// Set webhook for the bot
app.use(bot.webhookCallback('/telegram-bot'));

// Make the webhook listen to requests
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

bot.telegram.setWebhook(`${process.env.URL}/telegram-bot`);
