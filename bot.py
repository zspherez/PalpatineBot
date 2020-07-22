import asyncio
import requests
import discord
import json
import os


from discord.ext import commands, tasks

#bot = commands.Bot(command_prefix='t!')

bot = discord.Client()

activity=True

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(name="your bank accounts drain.", type=3))
    print(f'{bot.user.name} is running...')


@bot.event
async def on_message(message):
    if message.author != bot.user:
        if 'floor plan' in message.content.lower():
            if 'commons' in message.content.lower():
                await message.channel.send('Commons Floor Plans: https://discordapp.com/channels/678041940901625865/678067983376973845/735639699435159612')
            elif 'towers' in message.content.lower():
                await message.channel.send('Towers Floor Plans: https://discordapp.com/channels/678041940901625865/678067983376973845/735613872098246768')
            elif 'branscomb' in message.content.lower():
                await message.channel.send('Branscomb Floor Plans: https://discordapp.com/channels/678041940901625865/678067983376973845/725169006113325197')
        if 'https://groupme' in message.content.lower():
            await message.author.send('We do not allow advertising of GroupMe\'s in the Discord, your message has been deleted. If this is a house/floor GroupMe, please wait until the house channels have been created.')
            await message.delete()
        if 'vandy' in message.content.lower() and random.randint(0,19) == 7:
            await message.channel.send('fuck vandy')
            await message.channel.send('all my homies hate vandy')


bot.run(os.environ['TOKEN'])