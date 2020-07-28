import asyncio
import requests
import discord
import json
import os
import random
from discord.ext import commands
from airtable import Airtable

bot = commands.Bot(command_prefix='.')

activity=True

at = Airtable('appCYOvQRAC3kNBwp', api_key='keyBkVumCAYVGx3rI',table_name='Table 1')
at.get_all()
print(at)

bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(name="your bank accounts drain.", type=3))
    print(f'{bot.user.name} is running...')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency,2)*100))

@bot.command()
async def help(ctx):
    embed=discord.Embed(
        title = 'Emperor Palpatine',
        description = 'A bot to serve Vanderbilt discord servers!',
        colour = discord.Colour.dark_gold()
    )

    embed.set_footer(text='Created July 2020 by thecolellis#0001.')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/733788698277052438/733792565798764684/1200px-Vanderbilt_Commodores_logo.svg.png')
    embed.set_author(name='Vanderbot#9816',icon_url='https://cdn.discordapp.com/attachments/733788698277052438/733788776920383638/14c35b9dfc88eab5987613bd66063140.png')
    embed.add_field(name='My prefix:',value='\"`.`\"',inline=True)
    embed.add_field(name='Need help?',value='Type `.help` for assistance!',inline=True)
    embed.add_field(name='List of Commands',value='profile',inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def profile(ctx, *, arg):
    await bot.wait_until_ready()
    records = at.search('Name', arg)
    user = ctx.message.author
    pfp = user.avatar_url
    if not records:
        await ctx.send("User not found!")
    else:
        info = (records[0]['fields'])

        embed=discord.Embed(
            title = info['First Name'] + ' ' + info['Last Name'] + ' (' + info['Discord username with Discriminator'] + ')',
            colour = discord.Colour.dark_gold()
        )

        embed.set_footer(text='Information is updated daily.  Please message `thecoleellis#6969` if any errors are found.')
        embed.set_thumbnail(url=info['Portrait'])
        embed.set_author(name=user,icon_url=pfp)
        embed.add_field(name='Graduating Year',value=info['Graduating Year'],inline=True)
        embed.add_field(name='(Intended) Major',value=info['(Intended) Major'],inline=True)
        embed.add_field(name='College of Enrollment',value=info['College of Enrollment'],inline=True)
        embed.add_field(name='Dorm House', value=info['Dorm House'], inline=True)
        embed.add_field(name='Room Number', value=info['Room Number'], inline=True)
        embed.add_field(name='VU Visions Group', value=info['VU Visions Group'], inline=True)
        embed.add_field(name='Introduction',value=info['Introduction'],inline=False)
        embed.add_field(name='Socials',value='Snapchat: http://snapchat.com/add/' + info['Socials: Snapchat'] + ' \n Instagram: http://instagram.com/' + info['Socials: Instagram'] + ' \n Linkedin: ' + info['Socials: LinkedIn'],inline=False)

        await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if 'floor plan' in message.content.lower():
            if 'commons' in message.content.lower():
                await message.channel.send(
                    'Commons Floor Plans: https://discordapp.com/channels/678041940901625865/678067983376973845/735639699435159612')
            elif 'towers' in message.content.lower():
                await message.channel.send(
                    'Towers Floor Plans: https://discordapp.com/channels/678041940901625865/678067983376973845/735613872098246768')
            elif 'branscomb' in message.content.lower():
                await message.channel.send(
                    'Branscomb Floor Plans: https://discordapp.com/channels/678041940901625865/678067983376973845/725169006113325197')
        if 'https://groupme' in message.content.lower():
            await message.author.send(
                'We do not allow advertising of GroupMe\'s in the Discord, your message has been deleted. If this is a house/floor GroupMe, please wait until the house channels have been created.')
            await message.delete()
        if 'vandy' in message.content.lower():
            rand = random.randint(0, 14)
            print(rand)
            if rand == 7:
                await message.channel.send('fuck vandy')
                await message.channel.send('all my homies hate vandy')
        if 'emperor' in message.content.lower() or 'palpatine' in message.content.lower() or 'diermeier' in message.content.lower() or 'chancellor' in message.content.lower():
            rand = random.randint(0, 14)
            print(rand)
            if rand == 7:
                await message.channel.send(
                    'https://media.discordapp.net/attachments/699763540361478145/734157709770752131/image0.jpg')
                await message.channel.send('The Emperor is always watching...')
    await bot.process_commands(message)

bot.run(os.environ['TOKEN'])

