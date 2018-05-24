import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.voice_client import VoiceClient
import time

Client = discord.Client()
startup_extensions = ["Music"]
client = commands.Bot(command_prefix = "!")
chat_filter = ["SALAD"]
bypass_list = ["448968257979023379","448919227550793739"]



class Main_Commands():
    def __init__(self,bot):
        self.bot = bot

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if "448968257979023379" in [role.id for role in message.author.roles]:
            args = message.content.split("  ")
            #args[0] = !SAY
            #args[1] = Hey
            #args[2] = There
            #args[1:] = Hey There
            await client.send_message(message.channel, "%s" % ("  ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Sorry, you do not have the required role to execute this commad")
    if message.content.upper().startswith('!AMIADMIN'):
        if "448968257979023379" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "`You are an admin!`")
        else:
            await client.send_message(message.channel, "`You are not an admin`")
    contents = message.content.split("  ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "`HEY! Foul language is prohibited in this server`")
                except discord.errors.NotFound:
                    return

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '(): ()'.format(type(e).__name__, e)
            print('Failed to load extention ()\n()'.format(extension, exc))
                
client.run("NDQ4OTAyMTEyMTY0NzA4Mzcy.Dec9Wg.VSA26sV5kVI9UaBwn4JwcyJfn8o")
