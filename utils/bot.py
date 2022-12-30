import time
import motor.motor_asyncio as motor
import os
import re
import jishaku
import discord
import aiohttp
import sys
import traceback
from config import (
     OWNERS, RED_COLOR, EMOJIS, MONGO_DB_URL
)
from discord.ext import commands, tasks
from pymongo import UpdateOne
from utils.embed import success_embed
from utils.help import EpicBotHelp


class EpicBot(commands.AutoShardedBot):
    def __init__(self, beta: bool = False):
        self.app_cmds: dict = {}
        self.beta = beta
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(
            owner_ids=OWNERS,
            command_prefix=">",
            intents=intents,
            case_insensitive=True,
            allowed_mentions=discord.AllowedMentions.none(),
            strip_after_prefix=True,
            help_command=None,
            cached_messages=10000,
            activity=discord.Activity(type=discord.ActivityType.playing, name=">help | Antinuke"),
            shard_count=1 # remove this if your bot is under 1000 servers
        )
        cluster = motor.AsyncIOMotorClient(MONGO_DB_URL)
        self.session = aiohttp.ClientSession()
        self.cogs_loaded = False
        self.cache_loaded = False

        self.db = cluster['FluxBots']
        self.serverconfig = self.db['serverconfig']
        self.serverconfig_cache = []
      


        if not self.cogs_loaded:
            self.load_extension('jishaku')
            print("Loaded jsk!")
            self.loaded, self.not_loaded = self.loop.run_until_complete(self.load_extensions('./cogs'))
            self.cogs_loaded = True


    async def set_default_guild_config(self, guild_id):
        pain = {
            "_id": guild_id,
            "antinuke": False
        }
        self.serverconfig_cache.append(pain)
        return await self.get_guild_config(guild_id)

    async def get_guild_config(self, guild_id):
        for e in self.serverconfig_cache:
            if e['_id'] == guild_id:
                if "antinuke" not in e:
                    e.update({"antinuke": False})
                return e
        return await self.set_default_guild_config(guild_id)  

    @tasks.loop(seconds=1, reconnect=True)
    async def update_serverconfig_db(self):
            cancer = []
            for eee in self.serverconfig_cache:
                hmm = UpdateOne(
                    {"_id": eee['_id']},
                    {"$set": {
                        "antinuke": eee.get("antinuke", False)}},
                    upsert=True
                )
                cancer.append(hmm)
            if len(cancer) != 0:
                await self.serverconfig.bulk_write(cancer)
            self.last_updated_serverconfig_db = time.time()  

    @update_serverconfig_db.before_loop
    async def before_update_serverconfig_db(self):
        await self.wait_until_ready() 

    async def get_cache(self):
        cursor = self.serverconfig.find({})
        self.serverconfig_cache = await cursor.to_list(length=None)
        print(f"Server config cache has been loaded. | {len(self.serverconfig_cache)} configs")
  


    async def load_extensions(self, filename_):
        loaded = []
        not_loaded = {}
        i = 0
        total = 0
        for filename in os.listdir(filename_):
            if filename.endswith('.py'):
                total += 1
                h = f'{filename_[2:]}.{filename[:-3]}'
                try:
                    self.load_extension(h)
                    loaded.append(h)
                    i += 1
                except Exception as e:
                    not_loaded.update({h: e})
        print(f"Loaded {i}/{total} extensions from {filename_}")
        return loaded, not_loaded


  
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if message.content.lower() in [f'<@{self.user.id}>', f'<@!{self.user.id}>']:
            prefixes = await self.fetch_prefix(message)
            prefix_text = ""
            for prefix in prefixes:
                prefix_text += f"`{prefix}`, "
            prefix_text = prefix_text[:-2]
            return await message.reply(embed=success_embed(
                f"{EMOJIS['wave_1']} Hello!",
                f"My prefix{'es' if len(prefixes) > 1 else ''} for this server {'are' if len(prefixes) > 1 else 'is'}: {prefix_text}"
            ))

        await self.process_commands(message)

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.content == after.content or before.author.bot or not self.cache_loaded or not self.cogs_loaded:
            return
        self.dispatch("message", after)

    async def on_ready(self):
     

        print("""
         _            _        _           _             _               _          _
        /\ \         /\ \     /\ \       /\ \           / /\            /\ \       /\ \\
       /  \ \       /  \ \    \ \ \     /  \ \         / /  \          /  \ \      \_\ \\
      / /\ \ \     / /\ \ \   /\ \_\   / /\ \ \       / / /\ \        / /\ \ \     /\__ \\
     / / /\ \_\   / / /\ \_\ / /\/_/  / / /\ \ \     / / /\ \ \      / / /\ \ \   / /_ \ \\
    / /_/_ \/_/  / / /_/ / // / /    / / /  \ \_\   / / /\ \_\ \    / / /  \ \_\ / / /\ \ \\
   / /____/\    / / /__\/ // / /    / / /    \/_/  / / /\ \ \___\  / / /   / / // / /  \/_/
  / /\____\/   / / /_____// / /    / / /          / / /  \ \ \__/ / / /   / / // / /
 / / /______  / / /   ___/ / /__  / / /________  / / /____\_\ \  / / /___/ / // / /
/ / /_______\/ / /   /\__\/_/___\/ / /_________\/ / /__________\/ / /____\/ //_/ /
\/__________/\/_/    \/_________/\/____________/\/_____________/\/_________/ \_\/
        """)
        print(f"Logged in as {self.user}")
        print(f"Connected to: {len(self.guilds)} guilds")
        print(f"Connected to: {len(self.users)} users")
        print(f"Connected to: {len(self.cogs)} cogs")
        print(f"Connected to: {len(self.commands)} commands")
        print(f"Connected to: {len(self.emojis)} emojis")
        print(f"Connected to: {len(self.voice_clients)} voice clients")
        print(f"Connected to: {len(self.private_channels)} private_channels")

        embed = success_embed(
            "Bot is ready!",
            f"""
    **Loaded cogs:** {len(self.loaded)}/{len(self.loaded) + len(self.not_loaded)}
            """
        )
        if self.not_loaded:
            embed.add_field(
                name="Not loaded cogs",
                value="\n".join([f"`{cog}` - {error}" for cog, error in self.not_loaded.items()]),
                inline=False
            )
        me = self.get_channel(1017984464556654603) 
        
        await me.send(embed=embed)