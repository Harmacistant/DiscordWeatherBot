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

client.run(TOKEN)