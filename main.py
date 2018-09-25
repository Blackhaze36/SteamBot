#!/usr/bin/env python3
# Steam Bot. Will accept commands on discord and run LinuxGSM commands on local host
import discord
import subprocess

# create discord client
client = discord.Client()

# Token from https://discordapp.com/developers
TOKEN = 'NDkyNDkyMDkwNTc2NDcwMDE3.DoXixQ.Jore9QdvVTRHoVzJv2JW9JbexHY'

# Dictionary for LinuxGSM commands. !discord_command: ['LinuxGSM', 'command']
LGSMCommands = {
    '!css_start': ['/home/steam/LinuxGSM/cssserver', 'start'],
    '!css_stop': ['/home/steam/LinuxGSM/cssserver', 'stop'],
    '!css_restart': ['/home/steam/LinuxGSM/cssserver', 'restart'],
    '!ins_start': ['/home/steam/LinuxGSM/insserver', 'start'],
    '!ins_stop': ['/home/steam/LinuxGSM/insserver', 'stop'],
    '!ins_restart': ['/home/steam/LinuxGSM/insserver', 'restart'],
    '!win_dir': ['dir'] #For testing subprocess on windows
}

# Dictionary for internal discord commands. !discord_command: internal command
internalCommands = {

}

# Runs once bot is ready
@client.event
async def on_ready():
	try:
		# print bot information
		print(client.user.name)
		print(client.user.id)
		print('Discord.py Version: {}'.format(discord.__version__))

	except Exception as e:
		print(e)

# Runs once new message is read
@client.event
async def on_message(message):

    # Turns the message.content into a string
    discordInput = message.content

    # If the command starts with '!' and the message author is not the bot, continue.
    if discordInput[0:1] == '!' and message.author != client.user:

        # If message is a key in LGSMCommands, then run the value through subprocess
        if message.content in LGSMCommands:
            await client.send_message(message.channel, "Running LGSM command")
            subprocess.run(LGSMCommands.get(message.content))

        # Prints the LGSMCommands Dictionary to show the available commands
        elif message.content == '!help':
            for x in LGSMCommands:
                await client.send_message(message.channel, x)

        # "pings" the bot to respond
        elif message.content == '!ping':
            await client.send_message(message.channel, "Pong!")

        # Logs out bot and stops script
        elif message.content == '!stop':
            await client.send_message(message.channel, "Steam Bot shutting down")
            await client.logout()

        # If the commands starts with ! but isn't a command, reply with an error
        else:
            await client.send_message(message.channel, "Invalid Command")

    # If the message.content doesn't start with '!' or the message author is the bot, do nothing.
    else:
        return
# Starts bot
client.run(TOKEN)
