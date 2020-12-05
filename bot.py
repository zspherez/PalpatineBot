import asyncio
import json
import os
import random
import re

import discord
import requests
from discord.ext import commands
from discord.utils import get
from airtable import Airtable

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents)

activity = True

fgm = r"https?://(www.)?groupme"  # fuck groupme

at = Airtable(os.environ['AT'], api_key=os.environ['ATKEY'], table_name='Table 1')
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
    await ctx.send(f"Pong! {bot.latency * 1000:.03f}ms")

@bot.command(pass_context=True)
async def mergerole(ctx):
    print('running')
    r = get(ctx.message.guild.roles, name="Accepted")
    print(r)
    newrole = get(ctx.message.guild.roles, name="Committed")
    print(newrole)
    for member in ctx.message.guild.members:
        print(member)
        if r in member.roles:
            print('to add')
            await member.add_roles(newrole)
            print('adding')
    print('done')
        
        

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Emperor Palpatine',
        description='A bot to serve Vanderbilt discord servers!',
        colour=discord.Colour.dark_gold()
    )

    embed.set_footer(text='Created July 2020 by thecolellis#6969.')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/733788698277052438/733792565798764684/1200px-Vanderbilt_Commodores_logo.svg.png')
    embed.set_author(name='Emperor Palpatine#6411',
                     icon_url='https://images-ext-2.discordapp.net/external/runjMvzmXx2Q7dRXkr7r48j6VQTBOiu-agSsMDySZdY/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/735266441204334663/b55eabc51240ca749f1f5d73a0e78463.png?width=681&height=681')
    embed.add_field(name='My prefix:', value='\"`.`\"', inline=True)
    embed.add_field(name='Need help?', value='Type `.help` for assistance!', inline=True)
    embed.add_field(name='List of Commands', value='help \n newprofile \n ping \n profile', inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def newprofile(ctx):
    embed = discord.Embed(
        title='New Profile:',
        description='Click this link to set up your profile: https://vandyinfo.tech/links/discordprofile',
        colour=discord.Colour.dark_gold()
    )
    await ctx.send(embed=embed)


@bot.command()
async def profile(ctx, *, arg=None):
    await bot.wait_until_ready()
    if not arg:
        records = at.search('Discord username with Discriminator', str(ctx.message.author))
    else:
        records = at.search('Name', arg.lower())
    user = ctx.message.author
    pfp = user.avatar_url
    if not records:
        await ctx.send("User not found! Reminder that the bot only updates once daily.")
    else:
        info = (records[0]['fields'])

        embed = discord.Embed(
            title=info['First Name'] + ' ' + info['Last Name'] + ' (' + info[
                'Discord username with Discriminator'] + ')',
            colour=discord.Colour.dark_gold()
        )

        embed.set_footer(
            text='Information is updated daily.  Please message `thecoleellis#6969` if any errors are found.')
        embed.set_thumbnail(url=info['Portrait'])
        embed.set_author(name=user, icon_url=pfp)
        embed.add_field(name='Graduating Year', value=info['Graduating Year'], inline=True)
        embed.add_field(name='(Intended) Major', value=info['(Intended) Major'], inline=True)
        embed.add_field(name='College of Enrollment', value=info['College of Enrollment'], inline=True)
        embed.add_field(name='Dorm House', value=info['Dorm House'], inline=True)
        embed.add_field(name='Room Number', value=info['Room Number'], inline=True)
        embed.add_field(name='VU Visions Group', value=info['VU Visions Group'], inline=True)
        embed.add_field(name='Introduction', value=info['Introduction'], inline=False)
        snap = False
        insta = False
        if 'None Provided' not in info['Socials: Snapchat']:
            snap = True
        if 'None Provided' not in info['Socials: Instagram']:
            insta = True
        if snap and insta:
            embed.add_field(name='Socials', value='Snapchat: http://snapchat.com/add/' + info[
                'Socials: Snapchat'] + ' \n Instagram: http://instagram.com/' + info[
                                                      'Socials: Instagram'] + ' \n Linkedin: ' + info[
                                                      'Socials: LinkedIn'], inline=False)
        elif snap:
            embed.add_field(name='Socials',
                            value='Snapchat: http://snapchat.com/add/' + info['Socials: Snapchat'] + ' \n Instagram: ' +
                                  info['Socials: Instagram'] + ' \n Linkedin: ' + info['Socials: LinkedIn'],
                            inline=False)
        elif insta:
            embed.add_field(name='Socials',
                            value='Snapchat: ' + info['Socials: Snapchat'] + ' \n Instagram: http://instagram.com/' +
                                  info['Socials: Instagram'] + ' \n Linkedin: ' + info['Socials: LinkedIn'],
                            inline=False)

        await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if not message.author.bot:        
        if message.author.id == 700233926085443645:
            user = bot.get_user(214508201624862731)
            vrand = random.randint(0,16)
            print(f"vrand: {vrand}")
            if vrand == 8:
                await message.channel.send('no :hearts:')             
            await bot.get_channel(712069333257420821).send("another one <@!214508201624862731>")
            
        if 'he is always watching' in message.content.lower():
            await message.channel.send(
                'https://media.discordapp.net/attachments/699763540361478145/734157709770752131/image0.jpg')
            await message.channel.send('The Emperor is always watching...')
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
        if re.search(fgm, message.content.lower()) and message.channel.id != 747890842819231815:  # match groupme link and check not wrong channel
            await message.author.send(
                'We do not allow the posting of GroupMe links outside of the <#747890842819231815> channel, please repost your link there.')
            await message.delete()
        if 'vandy' in message.content.lower():
            rand = random.randint(0, 20)
            arand = random.randint(0, 29)
            print(f"rand: {rand}")
            print(f"arand: {arand}")
            if rand == 7 and message.author.id != 472229397085290506:
                await message.channel.send('fuck vandy')
                await message.channel.send('all my homies hate vandy')
            if arand == 15 and message.author.id == 472229397085290506:
                await message.channel.send('fuck vandy')
                await message.channel.send('all my homies hate vandy')
            if rand == 7 and arand != 15 and message.author.id == 472229397085290506:
                await message.channel.send('i would\'ve said it if it wasnt alissa smh')
        if 'emperor' in message.content.lower() or 'palpatine' in message.content.lower() or 'diermeier' in message.content.lower() or 'chancellor' in message.content.lower():
            rand = random.randint(0, 14)
            print(rand)
            if rand == 7:
                await message.channel.send(
                    'https://media.discordapp.net/attachments/699763540361478145/734157709770752131/image0.jpg')
                await message.channel.send('The Emperor is always watching...')
        if bot.user in message.mentions:
            await message.channel.send('no :)')
        if message.channel.id == 692841868777750638:
            await message.add_reaction('\N{THUMBS UP SIGN}')
            await message.add_reaction('\N{THUMBS DOWN SIGN}')
        if 'sam' in message.content.lower() and 'admin' in message.content.lower():
            await message.delete()
        if 'admin' in message.content.lower() and 'abuse' in message.content.lower():
            await message.delete()
    await bot.process_commands(message)


bot.run(os.environ['TOKEN'])
