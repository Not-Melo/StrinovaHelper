# Hours wasted: 5
# Update above whenever maintained.

import discord
import os
import asyncio

from itertools import cycle
from discord.ext import commands, tasks
from dotenv import load_dotenv
from colorama import Fore

# Load environment variables
load_dotenv()
Dtoken = os.getenv('TOKEN')


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')


@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands!")
    except:
        print(f'already synced')
    print(f"{Fore.GREEN}Connected to {client.user.name}!{Fore.RESET}")
    change_status.start()

# Load cogs
async def load_cogs():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

# Bot status cycle
status = cycle([
    "Play Strinova / Calabiyau"
])


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status), status=discord.Status.online))


async def main():
    async with client:
        try:
            await load_cogs()
        except Exception as e:
            print(f"Error loading cogs: {e}")
        await client.start(Dtoken)

# Run the main function
asyncio.run(main())