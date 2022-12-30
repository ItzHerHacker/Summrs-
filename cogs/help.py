import string
import discord
import asyncio
from utils.bot import EpicBot

from config import MAIN_COLOR
from discord.ext import commands
from datetime import datetime, timedelta
from views import help as vhelp #need big refactor

class HelpCommand(commands.HelpCommand):
    """Help command"""



    async def on_help_command_error(self, ctx, error) -> None:
        handledErrors = [
            commands.CommandOnCooldown, 
            commands.CommandNotFound
        ]

        if not type(error) in handledErrors:
            print("! Help command Error :", error, type(error), type(error).__name__)
            return await super().on_help_command_error(ctx, error)

    def command_not_found(self, string) -> None:
        raise commands.CommandNotFound(f"Command {string} is not found")

    async def send_bot_help(self, mapping) -> None:
        allowed = 5
        close_in = round(datetime.timestamp(datetime.now() + timedelta(minutes=allowed)))
        embed = discord.Embed(title = "Help Summrs", description="・ Prefix for this server is `>`\n・ Total commands: 20\n・ Type `>help <command | module>` for more info", color = MAIN_COLOR)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1017984464556654603/1017993581320994876/Picsart_22-08-23_10-02-03-612.png")
        embed.set_footer(text=f"Made with 💖 by Rao")
        embed.add_field(name="<:arrow:1009092510792040528>**Modules**", value="<:stolen_emoji:1016556767544623125><:stolen_emoji:1016556828982775868>Setup\n<:stolen_emoji:1016556767544623125><:stolen_emoji:1016556828982775868>Info\n<:stolen_emoji:1016556767544623125><:stolen_emoji:1016556828982775868>Mod", inline=True)     





        view = vhelp.View(mapping = mapping, ctx = self.context, homeembed = embed, ui = 2)
        message = await self.context.send(embed = embed, view = view)
        try:
            await asyncio.sleep(60*allowed)
            view.stop()
            await message.delete()
        except: pass

    async def send_command_help(self, command):
        cog = command.cog
        if "help_custom" in dir(cog):
            emoji, label, _ = cog.help_custom()
            embed = discord.Embed(title = f"{emoji} Help · {label} : {command.name}", description=f"<:stolen_emoji:1016556828982775868>**Command** : {command.name}\n{command.help}", url="https://discord.gg/Zfz4YKRmSd", color = MAIN_COLOR)
            params = ""
            for param in command.clean_params: 
                params += f" <{param}>"
            embed.add_field(name="Usage", value=f"{command.name}{params}", inline=False)
            embed.add_field(name="Aliases", value=f"{command.aliases}`")
            embed.set_footer(text="Remind : Hooks such as <> must not be used when executing commands.", icon_url=self.context.message.author.display_avatar.url)
            await self.context.send(embed=embed)

    async def send_cog_help(self, cog):
        if "help_custom" in dir(cog):
            emoji, label, _ = cog.help_custom()
            embed = discord.Embed(title = f"{emoji} Help ", url="https://discord.gg/Zfz4YKRmSd", color = MAIN_COLOR)
            for command in cog.get_commands():
                params = ""
                for param in command.clean_params: 
                    params += f" <{param}>"
                embed.add_field(name=f"<:stolen_emoji:1016556828982775868>{command.name}{params}", value=f"{command.help}\n\u200b", inline=False)
            embed.set_footer(text="Remind : Hooks such as <> must not be used when executing commands.", icon_url=self.context.message.author.display_avatar.url)
            await self.context.send(embed=embed)

    async def send_group_help(self, group):
        await self.context.send("Group commands unavailable.")
     

class Help(commands.Cog, name="help"):
    """Help commands."""
    def __init__(self, bot):
        self._original_help_command = bot.help_command

        attributes = {
            'name': "help",
            'aliases': ['h', '?'],
            'cooldown': commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user) # discordpy2.0
        } 

        bot.help_command = HelpCommand(command_attrs=attributes)
        bot.help_command.cog = self
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command

    def help_custom(self):
        emoji = '<a:heart2:1016558723986108426>'
        label = "Help"
        description = ""
        return emoji, label, description

def setup(bot):
	bot.add_cog(Help(bot))