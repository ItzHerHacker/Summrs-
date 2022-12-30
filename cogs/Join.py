import os
import discord
import aiohttp
from discord.ext import commands, tasks
from discord.colour import Color
import json
from utils.checks import getConfig, updateConfig



class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
          data = getConfig(guild.id)
          data["owner"] = guild.owner_id
          updateConfig(guild.id, data)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
      with open("config.json", "r") as f:
          data = json.load(f)

      del data["guilds"][str(guild.id)]

      with open("config.json", "w") as f:
          json.dump(data, f)
                 
                


def setup(client):
	client.add_cog(Join(client))