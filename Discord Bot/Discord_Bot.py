# Import Dependencies
import discord
from discord.ext import commands
import random
from datetime import datetime
import asyncio
from itertools import cycle
import json

# Import Files
import Data
from Data.key import Token

# Prefix
prefix = '!'

# Defines Client (BOT)
client = commands.Bot(command_prefix=prefix)
# Update Prefix
async def updatePrefix():
    await client.wait_until_ready()
    while client.is_ready():
        for guild in client.guilds:
            with open("Discord Bot/Servers/{guildname}.json".format(guildname=guild.name), 'r') as r:     # Opens JSON file in read mode
                client = commands.Bot(command_prefix=data['prefix'])

# Writes JSON file
def write_json(data, filename):
    with open(filename, 'w') as w:
        json.dump(data, w, indent=4, sort_keys=True)

# Writing Server Data to JSON file
async def acquireData():
    await client.wait_until_ready()
    while client.is_ready():
        for guild in client.guilds:
            with open("Discord Bot/Servers/{guildname}.json".format(guildname=guild.name), 'w') as w:     # Opens JSON file in write mode
                new_guild = {"members": {}, "text_channels": {}, "voice_channels": {}, "prefix": prefix}
                json.dump(new_guild, w, indent=4)     # Formats JSON file
            with open("Discord Bot/Servers/{guildname}.json".format(guildname=guild.name), 'r') as r:     # Opens JSON file in read mode
                data = json.load(r)     # loads readable JSON file
                text_channels = data['text_channels']     # Makes a certain arary editable
                voice_channels = data['voice_channels']     # Makes a certain arary editable
                members = data['members']
            for channel in guild.text_channels:
                if not channel.name in text_channels:
                    text_channels[channel.name] = channel.id     # Creates a key/value with channel name/channel id
            for channel in guild.voice_channels:
                if not channel.name in voice_channels:
                    voice_channels[channel.name] = channel.id     # Creates a key/value with channel name/channel id
            for member in guild.members:
                if not member.name in members:
                    members[member.name] = member.id     # Creates a key/value with channel name/channel id
            write_json(data, "Discord Bot/Servers/{guildname}.json".format(guildname=guild.name))     # Writes Data into JSON file
        await asyncio.sleep(5)     # Sets Delay for 5 seconds

# Change Bot Status
async def changeStatus():
    global status
    status = [
    'Prefix is <<!>>',
    'Mowing the Lawn'
    ]

    await client.wait_until_ready()
    statusCycle = cycle(status)     # Creates a Cycle from an Iterable
    while client.is_ready():     # Checks if Client is ONLINE
        Status = next(statusCycle)     # Cycles through List
        await client.change_presence(activity=discord.Game(Status))     # Sets Bot's Status
        await asyncio.sleep(20)     # Sets Delay for 20 seconds


# Log IN
@client.event
async def on_ready():     # Method (Ready) Expected By Client (Runs Once When Connected)
    LogOn_msg = '''
{botname} Started: {datetime}

{botname} is READY
Status: ONLINE
UserName: {botname}
ID: {botID}
'''

    print(LogOn_msg.format(botname=client.user.name, datetime=datetime.now().strftime('%A, %b %d | %X'), botID=client.user.id))

    for guild in client.guilds:
        with open("Discord Bot/Servers/{guildname}.json".format(guildname=guild.name), 'r') as r:
            data = json.load(r)     # loads readable JSON file
            text_channels = data['text_channels']     # Makes a certain arary editable
        msg = '{botname} is ONLINE'.format(botname=client.user.name)     # msg
        await client.get_channel(text_channels.get('x-\u00e6-a-xii')).send(msg)     # Sends msg


# Guild Join
@client.event
async def on_guild_join(server):
    print("Joining {guildname}".format(guildname=server.name))

# Member Join
@client.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        if str(channel) == 'new_members':
            await channel.send('Welcome to the Server {member}'.format(member=member.mention))

# Log OUT
@client.command()
async def logOff(ctx):
    msg = '\n{} is OFFLINE'.format(client.user.name)     # msg
    print('{} has Logged Off:'.format(client.user.name), datetime.now().strftime('%A, %b %d | %X'), 'by {}'.format(ctx.message.author), end='')
    await ctx.send(msg)     # Sends msg
    await client.logout()     # Logs Off

# Change Prefix
@client.command(aliases=['prefix'])
async def changePrefix(ctx):
    new_prefix = await client.wait_for('message', timeout=10.0)
    with open("Discord Bot/Servers/{guildname}.json".format(guildname=new_prefix.guild.name), 'r') as r:     # Opens JSON file in read mode
        data = json.load(r)     # loads readable JSON file
        changePrefix = data['prefix']     # Makes a certain arary editable
    changePrefix['prefix'] = new_prefix
    write_json(data, "Discord Bot/Servers/{guildname}.json".format(guildname=new_prefix.guild.name))     # Writes Data into JSON file


# Reply to Hello
@client.command()
async def greet(ctx):
    responses = [
        'Hello',
        "Hi",
    ]
    msg = '{greeting}! {pingUser}'.format(greeting=random.choice(responses), pingUser=ctx.message.author.mention)     # msg
    await ctx.send(msg)     # Sends msg

# Flip a Coin
@client.command()
async def flipcoin(ctx):
    responses = ['heads', 'tails']
    msg = random.choice(responses)     # Selects msg
    await ctx.send(msg)

# Magic 8 Ball
@client.command(aliases=['8ball'])
async def _8ball(ctx):
    responses = [
    'YES!!!',
    'NO',
    'Shit Nah!!!',
    'NEVER',
    'Perhaps',
    'Perhaybe',
    'Maybe',
    'Mayhaps',
    'Theoritically',
    'The future is bleak',
    'If that were to happen then Emily would have to grow bigger boobs that Brendan',
    ]

    msg = '🎱 {}'.format(random.choice(responses))     # Selects msg
    await ctx.send(msg)     # Sends msg

# Creates |) | ( |(
@client.command()
async def generatePP(ctx):
    await ctx.send('Enter Size')

    try:
        size = await client.wait_for('message', timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')

    kstmSize = {
        'conor': 0,
        'alex': 0,
        'damien': 5,
        'paul': 1000
    }
    try:
        length = '=' * int(size.content)     # Tries to multiply string by integer
    except:     # Error
        if size.content in kstmSize:
            length = '=' * int(kstmSize.get(size.content))
        else:
            await ctx.send('Enter a valid Integer')     # Sends Error msg
    msg = '8{}D'.format(length)     # Creates msg
    await ctx.send(msg)     # Sends msg


# Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Encryption Codes
encryptionCodes = {
    '1101': [1],
    '1102': [2],
    '1103': [3],
    '1104': [4],
    '1105': [5],
    '1120': [20],
    '1501': [21, 18, 24, 11, 10],
    '1502': [23, 10, 15, 1, 14],
    '1503': [9, 24, 14, 22, 6],
    '1504': [22, 3, 15, 22, 3],
    '1505': [1, 11, 8, 17, 9]
}

# Encyptes a Message
@client.command()
async def encrypt(ctx):
    await ctx.send('Enter Message to Encrypt')

    try:
        encrypt = await client.wait_for('message', timeout=60.0)
        await ctx.send('Enter one of the Encryption Codes')
        await ctx.send(sorted(encryptionCodes.keys()))
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')
    try:
        encryptionCode = await client.wait_for('message', timeout=30.0)
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')

    encryptionValues = encryptionCodes.get(encryptionCode.content)
    encryptList = list(encrypt.content)
    encryptlen = len(encryptList)

    encryptionValuesCycle = cycle(encryptionValues)
    encryptionValue = int(encryptionValues[0])

    for position in range(encryptlen):
        character = encryptList[position]
        if character in alphabet:
            alphabetIndex = alphabet.index(character)
            for i in range(encryptionValue):
                try:
                    encryptList[position] = alphabet[alphabetIndex+1]
                    character = encryptList[position]
                    alphabetIndex = alphabet.index(character)
                except:
                    encryptList[position] = 'a'
                    if i == encryptionValue-1:
                        break
                    character = encryptList[position]
                    alphabetIndex = alphabet.index(character)
                    encryptList[position] = alphabet[alphabetIndex+1]
        elif character == ' ':
            pass
        else:
            await ctx.send('{} is not in list'.format(character))
        encryptionValue = int(next(encryptionValuesCycle))

    await ctx.send(''.join(encryptList))
    await ctx.send('Encryption Code Used: {}'.format(encryptionCode.content))

# Decrypts a Message
@client.command()
async def decrypt(ctx):
    await ctx.send('Enter Message to Decrypt')
    
    try:
        decrypt = await client.wait_for('message', timeout=60.0)
        await ctx.send('Enter one of the Decryption Codes')
        await ctx.send(sorted(encryptionCodes.keys()))
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')

    try:
        decryptionCode = await client.wait_for('message', timeout=30.0)
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long')

    decryptionValues = encryptionCodes.get(decryptionCode.content)
    decryptList = list(decrypt.content)
    decryptlen = len(decryptList)

    decryptionValuesCycle = cycle(decryptionValues)
    decryptionValue = int(decryptionValues[0])

    for position in range(decryptlen):
        character = decryptList[position]
        if character in alphabet:
            alphabetIndex = alphabet.index(character)
            try:
                decryptList[position] = alphabet[alphabetIndex-decryptionValue]
            except:
                print('error IDFK')
        elif character == ' ':
            pass
        else:
            pass
        decryptionValue = next(decryptionValuesCycle)

    await ctx.send(''.join(decryptList))


# Tasks
client.loop.create_task(acquireData())
client.loop.create_task(changeStatus())

# Starts the Bot
client.run(Token)