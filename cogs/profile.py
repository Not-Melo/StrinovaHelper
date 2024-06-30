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
    @app_commands.command(name="make_profile", description="Allow users to view your stats")
    async def make_profile_cmd(self, interaction: discord.Interaction, friend_code: str, rank: str = "unranked"): # eh I don't feel like working on this part just yet...
        embed = discord.Embed(title="", color=0xFFFFFF)
        embed.set_footer(text="Maintained by the community.")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # Allow members to update their profile


async def setup(bot):
    await bot.add_cog(ProfileSystem(bot))
