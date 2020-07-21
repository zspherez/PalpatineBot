import asyncio
import requests
import discord
import json


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
        if 'vandy' in message.content.lower() or 'vanderbilt' in message.content.lower():
            await message.channel.send('fuck vandy')
            await message.channel.send('all my homies hate vandy')
        elif ('palpatine' in message.content.lower()) or ('emperor' in message.content.lower()) or ('diermeier' in message.content.lower()) or ('chancellor' in message.content.lower()):
            await message.channel.send('https://media.discordapp.net/attachments/699763540361478145/734157709770752131/image0.jpg')

bot.run('NzM1MjY2NDQxMjA0MzM0NjYz.XxdwQw.rS-OMXxR-vyPllg1OmZx_ZlNjVo')