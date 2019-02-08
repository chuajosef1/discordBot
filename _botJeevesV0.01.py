##########################################
#Imported Fuctions                       #
#Last Updated:                           #
#2/05/19                                 #
##########################################
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game


def keyGrab():
    keyList = []
    filename = "_key.txt"
    file = open(filename, "r")
    for line in file:
        keyList.append(line)
    return keyList


keyList = keyGrab()

##########################################
#API KEYS & GLOBAL VARIBLE               #
#Last Updated:                           #
#2/05/19                                 #
##########################################
# Grab from: "https://discordapp.com/developers/applications/"
#"XXXXXXXXXXXXXXXXXXXXXXX DISCORD TOKEN XXXXXXXXXXXXXXXXXXXXXXXXX"
TOKEN = keyList[0]
BOT_PREFIX = ("!", "?")

client = Bot(command_prefix=BOT_PREFIX)


##########################################
# Discord Bot Client Commands
# Description:
# This section is commands issued by the user.
# Last Updated:2/05/19
##########################################
@client.command(name='join',
                description="Joins a voice channel",
                pass_context=True)
async def join(context):
    vchannel = context.message.author.voice.channel
    await vchannel.connect()


@client.command(name='dc',
                description='Disconnects bot from voice channel',
                pass_context=True)
async def disconnect(context):
    vchannel = context.voice_client
    await vchannel.disconnect()

##########################################
# Discord Bot Client Events
# Description:
# This section is mainly for certain events that occur in discord
# Last Updated:2/05/19
##########################################
@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="Watching anime"))
    print("Logged in as " + client.user.name)


client.run(TOKEN)
