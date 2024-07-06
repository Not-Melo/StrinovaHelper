import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore
import asyncio
import os

class IT_HELP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded IT_help.py")

    @app_commands.command(name="tech_question", description="Having Strinova tech issues?")
    async def help_cmd(self, interaction: discord.Interaction, question: str):

        await interaction.response.defer()

        embed = discord.Embed(title="Sent the question to some tech people. 📤", description="Please note these people take time out of their day to help you so please respect them, also note some won't help with wechat questions and mainly focus on Strinova related issues. 📝")
        embed.set_footer(text="Maintained by the community.")
        await interaction.followup.send(embed=embed)

        channel = discord.utils.get(interaction.guild.text_channels, id=1259040049501179936)

        noti = discord.Embed(title=f"{interaction.user} asked a question... 📥", description=f"Question: {question}\n\n```\nUser ID: {interaction.user.id}\nUsername: {interaction.user.name}\n```")
        embed.set_footer(text="Maintained by the community.")
        await channel.send(embed=noti)



        


async def setup(bot):
    await bot.add_cog(IT_HELP(bot))
