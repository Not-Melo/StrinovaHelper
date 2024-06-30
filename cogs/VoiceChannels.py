import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
from colorama import Fore

class VoiceChannels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc_id_to_created_channel = {}  # Dictionary to track created channels
        self.empty_channel_check.start()  # Start the background task for checking empty channels

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} Loaded VoiceChannels cog")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel != after.channel:
            # Check if the member joined the specific VC ID
            target_vc_ids = [1256690651366424676, 1256690725123264584]
            guild = member.guild
            
            # Check if the member joined any of the target VCs
            if after.channel and after.channel.id in target_vc_ids:
                try:
                    # Attempt to create a new voice channel in the same category
                    category = after.channel.category
                    role = member.guild.get_role(1255588237217497138)
                    overwrites = {
                        guild.default_role: discord.PermissionOverwrite(connect=False),
                        role: discord.PermissionOverwrite(
                            connect=True,
                            speak=True,
                            stream=True,
                            use_soundboard=False,
                            use_voice_activation=True
                        )
                    }
                    channel_name = f"{member.display_name}'s Room"
                    try:
                        new_channel = await guild.create_voice_channel(
                            channel_name,
                            category=category,
                            user_limit=5,
                            overwrites=overwrites
                        )
                    except Exception as e:
                        print(f"{Fore.RED}[ ERROR ]{Fore.RESET} An error occurred: {e}")
                    
                    # Track the created channel
                    self.vc_id_to_created_channel[after.channel.id] = {
                        'channel_id': new_channel.id,
                        'creation_time': datetime.now()
                    }
                    
                    # Move the member to the new channel
                    await member.move_to(new_channel)
                
                except discord.Forbidden:
                    print(f"{Fore.RED}[ ERROR ]{Fore.RESET} Bot does not have permissions to create or move to a voice channel.")
                except discord.HTTPException as e:
                    print(f"{Fore.RED}[ ERROR ]{Fore.RESET} An error occurred: {e}")
            
            # Check if someone left the created channel and delete it if owner
            if before.channel and before.channel.id in self.vc_id_to_created_channel.keys():
                created_channel_data = self.vc_id_to_created_channel.get(before.channel.id)
                created_channel = guild.get_channel(created_channel_data['channel_id'])
                
                # Ensure the member who left is the owner and the channel is empty
                if created_channel and created_channel.owner and created_channel.owner.id == member.id and len(created_channel.members) == 0:
                    try:
                        await created_channel.delete()
                        self.vc_id_to_created_channel.pop(before.channel.id)
                    except discord.Forbidden:
                        print(f"{Fore.RED}[ ERROR ]{Fore.RESET} Bot does not have permissions to delete the voice channel.")
                    except discord.HTTPException as e:
                        print(f"{Fore.RED}[ ERROR ]{Fore.RESET} An error occurred: {e}")

    @tasks.loop(minutes=1)
    async def empty_channel_check(self):
        current_time = datetime.now()
        empty_channels_to_delete = []

        for vc_id, data in self.vc_id_to_created_channel.items():
            creation_time = data['creation_time']
            channel_id = data['channel_id']
            created_channel = self.bot.get_channel(channel_id)

            # Check if the channel has been empty for more than 3 minutes
            if (current_time - creation_time) > timedelta(minutes=3) and created_channel and len(created_channel.members) == 0:
                empty_channels_to_delete.append(vc_id)
        
        # Delete empty channels that have exceeded the time limit
        for vc_id in empty_channels_to_delete:
            try:
                channel_id = self.vc_id_to_created_channel[vc_id]['channel_id']
                channel_to_delete = self.bot.get_channel(channel_id)
                await channel_to_delete.delete()
                self.vc_id_to_created_channel.pop(vc_id)
                print(f"{Fore.GREEN}[ SUCCESS ]{Fore.RESET} Deleted empty channel: {channel_to_delete.name}")
            except discord.Forbidden:
                print(f"{Fore.RED}[ ERROR ]{Fore.RESET} Bot does not have permissions to delete the voice channel.")
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ ERROR ]{Fore.RESET} An error occurred: {e}")

    @empty_channel_check.before_loop
    async def before_empty_channel_check(self):
        await self.bot.wait_until_ready()
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} Empty channel check task started")

    def cog_unload(self):
        self.empty_channel_check.cancel()

async def setup(bot):
    await bot.add_cog(VoiceChannels(bot))

# Made with CHATGPT because I could not be bothered programming all that :3