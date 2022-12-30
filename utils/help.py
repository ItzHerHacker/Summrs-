import discord
import datetime
from discord.ext import commands
from utils.embed import error_embed
from typing import Mapping, Optional, List
from config import (
    EMOJIS, EMOJIS_FOR_COGS, MAIN_COLOR,
    EMPTY_CHARACTER, WEBSITE_LINK, SUPPORT_SERVER_LINK, INVITE_BOT_LINK
)


async def get_cog_help(ctx: commands.Context, cog_name: str) -> discord.Embed:
    if cog_name == "nsfw" and not ctx.channel.is_nsfw():
        return error_embed(
            f"{EMOJIS['tick_no']} Go away horny!",
            "Please go to a **NSFW** channel to see the commands."
        )
    cog = ctx.bot.get_cog(cog_name)
    return discord.Embed(
        title=f"{cog_name.title()} Category",
        description="**Here are all the commands:**\n\n" + "\n".join([f"{EMOJIS['cmd_arrow']} `{e.name}` • {e.help}" for e in cog.get_commands()]),
        color=MAIN_COLOR
    ).set_thumbnail(url=ctx.bot.user.display_avatar.url
    ).add_field(name=EMPTY_CHARACTER, value=f"[Invite Flux]({INVITE_BOT_LINK}) | [Support Server]({SUPPORT_SERVER_LINK})", inline=False)


async def get_command_help(ctx: commands.Context, command_name: str) -> discord.Embed:
    command = ctx.bot.get_command(command_name)
    if command.cog_name == "nsfw" and not ctx.channel.is_nsfw():
        return error_embed(
            f"{EMOJIS['tick_no']} Go away horny!",
            "Please go to a **NSFW** channel to see the command."
        )
    return discord.Embed(
        title=f"{command_name.title()} Help",
        description=f"""
{command.help}
**Usage:**
```
{ctx.clean_prefix}{command.name} {' '.join(['<' + str(param) + '>' for param in command.clean_params])}
```
**Aliases:** {','.join(['`' + str(alias) + '`' for alias in command.aliases])}
**Cooldown:** {0 if command._buckets._cooldown is None else command._buckets._cooldown.per} seconds
                    """,
        color=MAIN_COLOR,
        timestamp=datetime.datetime.utcnow()
    ).set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url
    ).set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.display_avatar.url
    ).set_thumbnail(url=ctx.bot.user.display_avatar.url
    ).add_field(name=EMPTY_CHARACTER, value=f"[Invite Flux]({INVITE_BOT_LINK}) | [Support Server]({SUPPORT_SERVER_LINK})", inline=False)


async def get_bot_help(ctx: commands.Context, mapping: Mapping[Optional[commands.Cog], List[commands.Command]]) -> discord.Embed:
    all_cogs = [cog for cog, cmds in mapping.items() if cog is not None and cog.qualified_name.islower() and len(cmds) > 0 and cog.qualified_name != "nsfw"]
    if ctx.channel.is_nsfw():
        all_cogs.append(ctx.bot.get_cog('nsfw'))
    return discord.Embed(
        title="Hey There!",
        description="**Here are all my categories:**\n\n"+"\n".join(
            [f"{EMOJIS_FOR_COGS[cog.qualified_name]} • **{cog.qualified_name.title()}** [ `{len(cog.get_commands())}` ]" for cog in all_cogs]),
        color=MAIN_COLOR,
        timestamp=datetime.datetime.utcnow()
    ).set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.display_avatar.url
    ).set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url
    ).add_field(name="Links:", value=f"""
[Support]({SUPPORT_SERVER_LINK}) | [Invite]({INVITE_BOT_LINK})
    """, inline=False
    ).set_thumbnail(url=ctx.bot.user.display_avatar.url)


async def get_commands_list(ctx: commands.Context, mapping) -> discord.Embed:
    embed = discord.Embed(
        title="All the commands:",
        description=f"Please use `{ctx.clean_prefix}help <command>` for more detailed information.",
        color=MAIN_COLOR,
        timestamp=datetime.datetime.utcnow()
    ).set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.display_avatar.url
    ).set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)

    for cog, commands_ in mapping.items():
        if cog is not None and cog.qualified_name == cog.qualified_name.lower():
            if cog.qualified_name == 'nsfw':
                value = "Please go to a NSFW channel to view this commands!" if not ctx.channel.is_nsfw() else ", ".join([f"`{command.name}`" for command in commands_])
            else:
                value = ", ".join([f"`{command.name}`" for command in commands_])
            embed.add_field(
                name=f"{EMOJIS_FOR_COGS[cog.qualified_name]} • {cog.qualified_name.title()}",
                value=value,
                inline=False
            )
    embed.add_field(name="Links:", value=f"""
[Support]({SUPPORT_SERVER_LINK}) | [Invite]({INVITE_BOT_LINK})
    """, inline=False)

    return embed


class HelpSelect(discord.ui.Select):
    def __init__(self, ctx: commands.Context, options):
        super().__init__(placeholder="Please select a category.", options=options)
        self.ctx = ctx

    async def callback(self, i: discord.Interaction):
        self.view.children[0].disabled = False
        embed = await get_cog_help(self.ctx, self.values[0])
        await i.message.edit(embed=embed, view=self.view)


class HelpMenu(discord.ui.View):
    def __init__(self, ctx: commands.Context, mapping):
        super().__init__(timeout=None)
        self.ctx = ctx
        self.mapping = mapping

    @discord.ui.button(label="Home", emoji="🏠", style=discord.ButtonStyle.blurple, disabled=True)
    async def home(self, button: discord.ui.Button, interaction: discord.Interaction):
        for item in self.children:
            item.disabled = False
        button.disabled = True
        embed = await get_bot_help(self.ctx, self.mapping)
        await interaction.message.edit(embed=embed, view=self)

    @discord.ui.button(label="All Commands", emoji="📜", style=discord.ButtonStyle.blurple)
    async def commands_list(self, button: discord.ui.Button, interaction: discord.Interaction):
        for item in self.children:
            item.disabled = False
        button.disabled = True
        embed = await get_commands_list(self.ctx, self.mapping)
        await interaction.message.edit(embed=embed, view=self)

    @discord.ui.button(label="Delete Menu", emoji='🛑', style=discord.ButtonStyle.danger)
    async def delete_menu(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.message.delete()

    async def interaction_check(self, interaction: discord.Interaction):
        if interaction.user == self.ctx.author:
            return True
        await interaction.response.send_message("Not your command ._.", ephemeral=True)


class EpicBotHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping: Mapping[Optional[commands.Cog], List[commands.Command]]):
        embed = await get_bot_help(self.context, mapping)
        all_cogs = [cog for cog, cmds in mapping.items() if
                    cog is not None and cog.qualified_name.islower() and len(cmds) > 0 and cog.qualified_name != "nsfw"]
        if self.context.channel.is_nsfw():
            all_cogs.append(self.context.bot.get_cog('nsfw'))
        view = HelpMenu(self.context, mapping)
        select = HelpSelect(
            self.context,
            [discord.SelectOption(
                label=cog.qualified_name.title(),
                emoji=EMOJIS_FOR_COGS[cog.qualified_name],
                value=cog.qualified_name,
                description=cog.description
            ) for cog in all_cogs]
        )
        view.add_item(select)
        await self.context.reply(embed=embed, view=view)

    async def send_cog_help(self, cog):
        return await self.context.reply(embed=await get_cog_help(self.context, cog.qualified_name))

    async def send_command_help(self, command):
        return await self.context.reply(embed=await get_command_help(self.context, command.name))

    async def send_error_message(self, error):
        return await self.context.reply(embed=error_embed(f"{EMOJIS['tick_no']} Error", error))

    async def send_group_help(self, group):
        prefix = self.context.clean_prefix
        embed = discord.Embed(
            title=f"Group command help: `{group.qualified_name}`",
            description=group.description,
            color=MAIN_COLOR
        ).set_author(name=self.context.bot.user.name, icon_url=self.context.bot.user.avatar.url
        ).set_footer(text=f"Requested by: {self.context.author}", icon_url=self.context.author.display_avatar.url)

        embed.add_field(
            name="Subcommands:",
            value="\n".join([f"`{prefix}{cmd.qualified_name}{' ' + cmd.signature if cmd.signature else ''}` - {cmd.help}" for cmd in group.commands]),
            inline=False
        )
        return await self.context.reply(embed=embed)