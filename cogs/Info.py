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
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded Info.py")

    @app_commands.command(name="char_info", description="Learn about the characters.")
    @app_commands.choices(choices=[
        app_commands.Choice(name="Ming", value="Ming"),
        app_commands.Choice(name="Michele", value="Michele"),
        app_commands.Choice(name="Example", value="Example"),
    ])
    async def info_cmd(self, interaction: discord.Interaction, choices: app_commands.Choice[str]):
        # json open file

        Char_color=0xfffff # Example replace with json

        Chibi_Thumbnail="https://i.pinimg.com/736x/34/05/27/340527254d64e5ae5261ddbb95ae34de.jpg"

        ## Wakenings from JSON ##
        
        W1="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        W2="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        W3="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

        ## Passive & Ult from JSON ##
        Passive = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        Ult = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

        # | Back Story from JSON | #
        back_story="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl rhoncus mattis rhoncus urna neque viverra. Tellus orci ac auctor augue. Ridiculus mus mauris vitae ultricies leo integer malesuada. Aliquet enim tortor at auctor urna."

        embed = discord.Embed(title=f"{choices.value} | Character Information", color=Char_color)
        embed.add_field(name="Wakening 1", value=f"{W1}", inline=True)
        embed.add_field(name="Wakening 2", value=f"{W2}", inline=True)
        embed.add_field(name="Wakening 3", value=f"{W3}", inline=True)
        embed.add_field(name="Passive", value=f"{Passive}", inline=True)
        embed.add_field(name="Ult", value=f"{Ult}", inline=True)
        embed.add_field(name=f"{choices.value}'s Back story", value=f"{back_story}", inline=False)
        embed.set_thumbnail(url=Chibi_Thumbnail)
        await interaction.response.send_message(embed=embed, ephemeral=False)


async def setup(bot):
    await bot.add_cog(InfoSystem(bot))
