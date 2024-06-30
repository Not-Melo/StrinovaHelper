import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore
import asyncio
import os

class InfoSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded help.py")

    @app_commands.command(name="help", description="helpful command to teach you about the bot.")
    async def help_cmd(self, interaction: discord.Interaction):
        embed = discord.Embed(title="🆘 | Helpful command", color=0xFFFFFF)
        embed.add_field(
            name="/make_profile", 
            value="This command is not yet ready for use...",
            inline=True
            )
        embed.set_footer(text="Maintained by the community.")
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(InfoSystem(bot))
