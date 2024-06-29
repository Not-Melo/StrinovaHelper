import discord
import random
from discord.ext import commands
from discord import app_commands
from colorama import Fore
import asyncio
import os

class ProfileSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded profile.py")

    # Make a profile system so people can search for there friend's friend code.

    # Allow members to update their profile


async def setup(bot):
    await bot.add_cog(ProfileSystem(bot))
