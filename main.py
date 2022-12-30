import os
os.system("pip install git+https://github.com/Nirlep5252/discord.py")
from handler.app_commands import InteractionContext
from logging import basicConfig, INFO
import jishaku
from config import BOT_TOKEN, OWNERS
from utils.bot import EpicBot
from os import environ
from handler import InteractionClient


basicConfig(level=INFO)

client = EpicBot()
InteractionClient(client)
# If you have beta token and beta mongodb link setup
# what you can do is just pass the kwarg beta as true eg: "client = EpicBot(beta=True)"
# and it'll use that token and mongo link
# so when testing locally it wont use the main bots token
# :)
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

@client.listen('on_global_commands_update')
async def on_global_commands_update(commands: list):
    print(f'{len(commands)} Global commands updated')


@client.listen('on_guild_commands_update')
async def on_guild_commands_update(commands: list, guild_id: int):
    print(f"{len(commands)} Guild commands updated for guild ID: {guild_id}")


@client.listen('on_app_command')
async def on_app_command(ctx: InteractionContext):
    print(f"{ctx.command.name} app command used by {ctx.author}")

if __name__ == '__main__':
    client.run(BOT_TOKEN)