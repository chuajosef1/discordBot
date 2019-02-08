##########################################
#Imported Fuctions                       #
#Last Updated:                           #
#02/05/19                                #
##########################################
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game


##########################################
#Defined Functions                       #
#Last Updated:                           #
#02/08/19                                #
##########################################
def keyGrab():
    keyList = []
    filename = "_key.txt"
    file = open(filename, "r")
    for line in file:
        keyList.append(line)
    return keyList


keyList = keyGrab()


def answersGrab():
    answers = []
    filename = "_answers.txt"
    file = open(filename, "r")
    for line in file:
        answers.append(line)
    return answers


##########################################
#API KEYS & GLOBAL VARIBLE               #
#Last Updated:                           #
#02/05/19                                #
##########################################
# Grab from: "https://discordapp.com/developers/applications/"
# "XXXXXXXXXXXXXXXXXXXXXXX DISCORD TOKEN XXXXXXXXXXXXXXXXXXXXXXXXX"
TOKEN = keyList[0]
BOT_PREFIX = ("!", "?")

client = Bot(command_prefix=BOT_PREFIX)

##########################################
# Discord Bot Client Generic Commands
# Description:
# This section is commands issued by the user.
# Last Updated:02/08/19
##########################################


@client.command(name='8ball',
                description='Ask the mystic 8-Ball a question.',
                pass_context=True)
async def eight_ball(context):
    answerList = answersGrab()
    channel = context.message.channel
    author = context.message.author.mention
    response = random.randrange(len(answerList))
    await channel.send(answerList[response].rstrip() + " " + str(author))


##########################################
# Discord Bot Client Voice Commands
# Description:
# This section is commands issued by the user.
# Last Updated:02/08/19
##########################################
@client.command(name='join',
                description="Joins a voice channel",
                pass_context=True)
async def join(context):
    vchannel = context.message.author.voice.channel
    await vchannel.connect()


##########################################
# Discord Bot Client Events
# Description:
# This section is mainly for certain events that occur in discord
# Last Updated:02/05/19
##########################################
@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="Watching anime"))
    print("Logged in as " + client.user.name)


client.run(TOKEN)
