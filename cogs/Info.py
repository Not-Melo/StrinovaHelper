import discord
import json
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
    async def info_cmd(self, interaction: discord.Interaction, Search: str):
        
        with open(f"/JSON/characters.json", "r") as file:
            Char_Info = json.load(file)
        
        Search = Search.lower()

        if Search in Char_Info["Strinova Characters"]:

            char_data = Char_Info["Strinova Characters"][Search]
            char_type = char_data["Type"]
            char_color = char_data["Char_color"]
            chibi_thumbnail = char_data["Chibi_Thumbnail"]
            w1 = char_data["W1"]
            w2 = char_data["W2"]
            w3 = char_data["W3"]
            passive = char_data["Passive"]
            ult = char_data["Ult"]
            back_story = char_data["back_story"]

            embed = discord.Embed(title=f"{Search} | Character Information", color=char_color)
            embed.add_field(name="Wakening 1", value=f"{w1}", inline=True)
            embed.add_field(name="Wakening 2", value=f"{w2}", inline=True)
            embed.add_field(name="Wakening 3", value=f"{w3}", inline=True)
            embed.add_field(name="Passive", value=f"{passive}", inline=True)
            embed.add_field(name="Ult", value=f"{ult}", inline=True)
            embed.add_field(name=f"{Search}'s Back story", value=f"{back_story}", inline=False)
            embed.set_footer(text=f"Type: {char_type}")
            embed.set_thumbnail(url=chibi_thumbnail)
            await interaction.response.send_message(embed=embed, ephemeral=False)
        else:
            embed = discord.Embed(title="Error", description=f"Could not find information for '{Search}'.")
            embed.add_field(name="Did you spell something wrong?", value="Please check the list of characters.")
            embed.add_field(name="List of characters...", value="```\nMichele | Ming | Maddelena\nYvette | Merideith | Celestia\nKokona | Lawine | Audry\nNobunaga | Reiichi | Fuschia\nFlavia | Kanami | Bai Mo\n```")
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(InfoSystem(bot))
