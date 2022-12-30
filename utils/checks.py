import json
from discord.ext import commands
import time
import asyncio


def getConfig(guildID):
    with open("config.json", "r") as config:
        data = json.load(config)
    if str(guildID) not in data["guilds"]:
        defaultConfig = {
            "owner": " ",
            "Punishment": "1",
            "whitelist": [],
            "log_channel": "",
            "mod": [],
            "admin": []
        }
        updateConfig(guildID, defaultConfig)
        return defaultConfig
    return data["guilds"][str(guildID)]


def updateConfig(guildID, data):
    with open("config.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildID)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("config.json", "w") as config:
        config.write(newdata)



def guild_owner_only():
    async def predicate(ctx):
        return ctx.author == ctx.guild.owner
    return commands.check(predicate)


def is_mod():
    async def predicate(ctx):
        guild = ctx.guild
        g = getConfig(guild.id)
        mod = g['mod']
        admin = g['admin']
        return ctx.author == ctx.guild.owner or ctx.author.id in mod or ctx.author.id in admin
    return commands.check(predicate)

def is_admin():
    async def predicate(ctx):
        guild = ctx.guild
        g = getConfig(guild.id)
        admin = g['admin']
        return ctx.author == ctx.guild.owner or ctx.author.id in admin
    return commands.check(predicate)