#!/usr/bin/env python3
import os, discord, warnings, logging

if 'DISCORD_TOKEN' not in os.environ:
    logging.log(level=logging.ERROR, msg="DISCORD_TOKEN environment variable not set.")
    os.environ['DISCORD_TOKEN'] = input("Please enter the DISCORD_TOKEN value here: ")
    #raise SystemExit("DISCORD_TOKEN environment variable not set.  Please set this variable in order to load the bot.")

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(
        f'Hello, {member.name}, welcome to the server!  I am the weather bot.'
    )
    await member.dm_channel_send(
        f'I provide monitoring services for sever or extreme weather events, based on zip code.  If you\'d like to know more, just say \'help\' to see what all I can do!'
    )

client.run(TOKEN)