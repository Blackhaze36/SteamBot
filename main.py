#!/usr/bin/env python3
# Steam Bot. Will run commands on PieBox through messages on discord
import discord
import subprocess

# create discord client
client = discord.Client()

# token from https://discordapp.com/developers
TOKEN = 'NDkyNDkyMDkwNTc2NDcwMDE3.DoXixQ.Jore9QdvVTRHoVzJv2JW9JbexHY'

#Dictionary for all our commands. discordCommand/LGSMCommand
commands = {
    'css_start': ['/home/steam/LinuxGSM/cssserver', 'start'],
    'css_stop': ['/home/steam/LinuxGSM/cssserver', 'stop'],
    'css_restart': ['/home/steam/LinuxGSM/cssserver', 'restart'],
    'ins_start': ['/home/steam/LinuxGSM/insserver', 'start'],
    'ins_stop': ['/home/steam/LinuxGSM/insserver', 'stop'],
    'ins_restart': ['/home/steam/LinuxGSM/insserver', 'restart'],
    'win_dir': ['dir'] #For testing subprocess on windows
}

# ran when bot is ready
@client.event
async def on_ready():
	try:
		# print bot information
		print(client.user.name)
		print(client.user.id)
		print('Discord.py Version: {}'.format(discord.__version__))

	except Exception as e:
		print(e)

# on new message
@client.event
async def on_message(message):

    # Checks if the message was sent by the bot, if so does nothing.
    # This prevents the bot from responding to itself
    if message.author == client.user:
        return

    # Used to test the bots responce time
    elif message.content == "!ping":
        await client.send_message(message.channel, "Pong!")

    # Logs outs the bot and stops script
    elif message.content == '!stop':
        await client.send_message(message.channel, "Steam Bot shutting down")
        await client.logout()

    # Checks if message.content is a key in command and then runs it with subprocess
    elif message.content in commands:
        await client.send_message(message.channel, "Running command")
        subprocess.run(commands.get(message.content))

    #Catches anything that not a command
    else:
        await client.send_message(message.channel, "Invalid Command")

# start bot
client.run(TOKEN)
