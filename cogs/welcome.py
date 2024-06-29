import discord
import random
from discord.ext import commands
from discord import app_commands
from colorama import Fore
import asyncio
import os

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded welcome.py")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        colors = [0xFFC0CB, 0xA020f0, 0x89CFF0]
        embed = discord.Embed(
            title=f"Welcome to the server, {member.name}!",
            description=f"We are glad to have you here, {member.mention}.",
            color=random.choice(colors)
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="ℹ️ About Us", value="We help new Strinova users figure out bugs and recent fixes we came up with. Not only that we study each game we play and give new information on plays that may turn your game around.")
        embed.set_footer(text=f"Joined {member.guild.name} | {member.guild.member_count} members")

        channel = discord.utils.get(member.guild.text_channels, name="✢-welcome")
        
        if channel is not None:
            await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
