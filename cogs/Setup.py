
import discord
import re
import urllib
import typing as t

from discord.ext import commands
import emojis
from datetime import datetime
from re import search
from collections import Counter
from typing import Optional, Union
from utils.message import wait_for_msg
from utils.embed import error_embed, success_embed
from utils.checks import getConfig, updateConfig, is_admin
from config import (
    BADGE_EMOJIS, EMOJIS, RED_COLOR
)
from utils.bot import EpicBot

prefix = ">"

class AntiAltsSelectionView(discord.ui.View):
    def __init__(self, context):
        super().__init__(timeout=None)
        self.level = 0
        self.context = context
        self.cancelled = False

    @discord.ui.select(placeholder="Punishment", options=[
        discord.SelectOption(
            label="Ban",
            description="Set antinuke punishment to ban",
            value='1', emoji='<:bt_Security:1008936077186310144>'
        ),
        discord.SelectOption(
            label="Kick",
            description="Set antinuke punishment to kick",
            value='2', emoji='<:bt_Security:1008936077186310144>'
        ),
        discord.SelectOption(
            label="None",
            description="Set antinuke punishment to none",
            value='3', emoji='<:bt_Security:1008936077186310144>'
        ),
    ])
    async def callback(self, select: discord.ui.Select, interaction: discord.Interaction):
        if interaction.user != self.context.author:
            return await interaction.response.send_message("You cannot interact in someone else's interaction.", ephemeral=True)
        self.level = int(select.values[0])
        await interaction.response.send_message(f"Antinuke Punishment **{select.values[0]}** has been selected. Please click the `Next` button to continue.", ephemeral=True)

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.red)
    async def cancel(self, b: discord.ui.Button, i: discord.Interaction):
        if i.user != self.context.author:
            return await i.response.send_message("You cannot interact in someone else's interaction.", ephemeral=True)
        self.cancelled = True
        self.stop()

    @discord.ui.button(label='Next', style=discord.ButtonStyle.green)
    async def next(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user != self.context.author:
            return await interaction.response.send_message("You cannot interact in someone else's interaction.", ephemeral=True)
        if self.level == 0:
            return await interaction.response.send_message("Please select a punishment ", ephemeral=True)
        self.stop()

class AntiNukeSelectionView(discord.ui.View):
    def __init__(self, context):
        super().__init__(timeout=None)
        self.leve = 0
        self.context = context
        self.cancelled = False

    @discord.ui.select(placeholder="Whitelist", options=[
        discord.SelectOption(
            label="Whitelist Add",
            description="Add a user to antinuke whitelist",
            value='1', emoji='<:arrow:1009092510792040528>'
        ),
        discord.SelectOption(
            label="Whitelist Remove",
            description="Rremoves a user from antinuke whitelist",
            value='2', emoji='<:arrow:1009092510792040528>'
        ),
        discord.SelectOption(
            label="Whitelist Show",
            description="Shows List",
            value='3', emoji='<:arrow:1009092510792040528>'
        ),
    ])
    async def callback(self, select: discord.ui.Select, interaction: discord.Interaction):
        if interaction.user != self.context.author:
            return await interaction.response.send_message("You cannot interact in someone else's interaction.", ephemeral=True) 
        self.leve = int(select.values[0])
        if self.leve == 1:
          await interaction.response.send_message("Mention The user", ephemeral=True)
          self.stop()
        if self.leve == 2:
          await interaction.response.send_message("Mention The user", ephemeral=True)
          self.stop()
        if self.leve == 3:
          self.stop()  


class ModAdd(discord.ui.View):
    def __init__(self, context):
        super().__init__(timeout=None)
        self.leve = 0
        self.context = context
        self.cancelled = False

    @discord.ui.select(placeholder="Whitelist", options=[
        discord.SelectOption(
            label="Add",
            description="Add a user",
            value='1', emoji='<:arrow:1009092510792040528>'
        ),
        discord.SelectOption(
            label="Remove",
            description="Removes a user",
            value='2', emoji='<:arrow:1009092510792040528>'
        ),
        discord.SelectOption(
            label="Show",
            description="Shows List",
            value='3', emoji='<:arrow:1009092510792040528>'
        ),
    ])
    async def callback(self, select: discord.ui.Select, interaction: discord.Interaction):
        if interaction.user != self.context.author:
            return await interaction.response.send_message("You cannot interact in someone else's interaction.", ephemeral=True) 
        self.leve = int(select.values[0])
        if self.leve == 1:
          await interaction.response.send_message("Mention The user", ephemeral=True)
          self.stop()
        if self.leve == 2:
          await interaction.response.send_message("Mention The user", ephemeral=True)
          self.stop()
        if self.leve == 3:
          self.stop()  
    
      

class Setup(commands.Cog, description="Keep your server safe"):
    def __init__(self, client: EpicBot):
        self.client = client

    """Antinuke Setup commands"""  

    def help_custom(self):
		      emoji = '<a:durex_setting:1012951132659777537>'
		      label = "Antinuke"
		      description = "All Commands Related To Server Security"
		      return emoji, label, description    

    @commands.command(help="Antinuke System Summrs", aliases=['antiwizz', 'anti'])
    @commands.cooldown(3, 30, commands.BucketType.user)
    @is_admin()
    async def antinuke(self, ctx, config=None, setting: Union[discord.TextChannel, discord.Role, int, str] = None):
        g = getConfig(ctx.guild.id)

        info_embed = success_embed(
            f"{BADGE_EMOJIS['bot_mod']}  Anti Nuke",
            f"""
Anti Nuke is current **{'Enabled'}**.
**Punishment** `{g['Punishment']}`
**Log channel:** {'<#'+str(g['log_channel'])+'>'}
            """
        ).add_field(
            name="1 - Ban",
            value="Set antinuke punishment to ban",
            inline=True
        ).add_field(
            name="2 - Kick",
            value="Set antinuke punishment to Kick",
            inline=True
        ).add_field(
            name="3 - None",
            value="Set antinuke punishment to None",
            inline=True
        ).add_field(
            name="Commands:",
            value=f"""
- `{prefix}antinuke setup` - To enable/disable anti-nuke protection.
- `{prefix}antinuke channel #channel` - To change the log channel.
- `{prefix}whitelist` - To add/remove members from anti-nuke whitelist.
                """
        )

        if config is None:
            return await ctx.reply(embed=info_embed)

        if config.lower() == 'setup':

            log_channel = None

            view = AntiAltsSelectionView(context=ctx)
            msg = await ctx.reply(f"""
**Anti Nuke setup**
- {EMOJIS['idle']} Punishment.
- {EMOJIS['dnd']} Log channel.
Please select a protection level.
                                """, view=view)

            await view.wait()

            if view.cancelled:
                return await msg.edit(
                    content="",
                    embed=discord.Embed(title=f"{EMOJIS['tick_no']} Cancelled", color=RED_COLOR),
                    view=None
                )
            await msg.edit(f"""
**Anti Nuke setup**
- {EMOJIS['online']} Punishment `{view.level}`
- {EMOJIS['idle']} Log channel.
Please enter a log channel.
Type `create` to automatically create a channel.
Type `cancel` to cancel the command.
                            """, view=None)
            m = await wait_for_msg(ctx, 60, msg)
            if m == 'pain':
                return
            if m.content.lower() == 'create':
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
                }
                created_channel = await ctx.guild.create_text_channel('summrs-log', overwrites=overwrites)
                log_channel = created_channel.id
            else:
                try:
                    lul_channel = await commands.TextChannelConverter().convert(ctx=ctx, argument=m.content)
                    log_channel = lul_channel.id
                except commands.ChannelNotFound:
                    return await msg.reply(content="", embed=error_embed(
                        f"{EMOJIS['tick_no']} Not found!",
                        f"I wasn't able to find the channel {m.content}, please try again."
                    ), view=None)

            await msg.edit(f"""
**Setup complete**
Here are you settings:
- {EMOJIS['online']} Level: `{view.level}`
- {EMOJIS['online']} Log channel: <#{log_channel}>
                            """)

            g['Punishment'] = int(view.level)
            g['log_channel'] = log_channel
            updateConfig(ctx.guild.id, g)
            return


        if config.lower() == 'channel':
            if config is None:
                return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Invalid Usage", f"Please use `{prefix}antinuke channel #channel`"))
            if not isinstance(setting, discord.TextChannel):
                return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Not found!", f"I wasn't able to find channel {setting}, please try again."))
            g['log_channel'] = setting.id
            updateConfig(ctx.guild.id, g)
            return await ctx.reply(embed=success_embed(
                f"{EMOJIS['tick_yes']} Updated!",
                f"The log channel has been updated to {setting.mention}"
            ))

        else:
            return await ctx.reply(embed=info_embed)      

    @commands.command(help="Antinuke System Summrs Whitelist", aliases=['wl'])
    @commands.cooldown(3, 30, commands.BucketType.user)
    @is_admin()
    async def whitelist(self, ctx, config=None, setting: Union[discord.Member, discord.Role, int, str] = None):
        g = getConfig(ctx.guild.id)
        whitelisted = g["whitelist"]


        if config is None:


            view = AntiNukeSelectionView(context=ctx)
            msg = await ctx.reply(f"""
**Anti Nuke Whitelist**
- {EMOJIS['idle']} Whitelist.
Please select a option.
                                """, view=view)

            await view.wait()

            if view.cancelled:
                return await msg.edit(
                    content="",
                    embed=discord.Embed(title=f"{EMOJIS['tick_no']} Cancelled", color=RED_COLOR),
                    view=None
                )
            if view.leve == 1:  

                m = await wait_for_msg(ctx, 60, msg)
                me = await commands.MemberConverter().convert(ctx=ctx, argument=m.content)
                if me.id in whitelisted:
                  await ctx.reply(f"<@{me.id}> is already in whitelist")
                else: 
                  g["whitelist"].append(me.id)
                  updateConfig(ctx.guild.id, g)                  
                  await ctx.reply(f"<@{me.id}> Has Been added to whitelist")

            elif view.leve == 2:
                m = await wait_for_msg(ctx, 60, msg)
                me = await commands.MemberConverter().convert(ctx=ctx, argument=m.content)
                if me.id not in whitelisted:
                  await ctx.reply(f"<@{me.id}> is not in whitelist")
                else: 
                  g["whitelist"].remove(me.id)
                  updateConfig(ctx.guild.id, g)  
                  await ctx.reply(f"<@{me.id}> Has Been Removed From whitelist")

            elif view.leve == 3:
                result = ' '
                for i in whitelisted:
                  user2 = self.client.get_user(i)
                  if user2 == None:
                        user = 'Unable to Fetch Name'
                  else:
                        user = user2.mention
                  result += f"{user}: {i}\n"
                if whitelisted == []:
                  return await ctx.send("There are no whitelisted users in this server, do `>whitelist` to whitelist a user of your choice!")
                else:
                    embed = discord.Embed(title=f'Whitelisted users for {ctx.guild.name}', description=result,
                                          color=0x2F3136)
                    await ctx.send(embed=embed)

    @commands.command(help="Add Mod Function", aliases=['am'])
    @commands.cooldown(3, 30, commands.BucketType.user)
    @is_admin()
    async def mod(self, ctx, config=None, setting: Union[discord.Member, discord.Role, int, str] = None):
        g = getConfig(ctx.guild.id)
        mod = g["mod"]


        if config is None:


            view = ModAdd(context=ctx)
            msg = await ctx.reply(f"""
**Bot Mod**
- {EMOJIS['idle']} Mod.
Please select a option.
                                """, view=view)

            await view.wait()

            if view.cancelled:
                return await msg.edit(
                    content="",
                    embed=discord.Embed(title=f"{EMOJIS['tick_no']} Cancelled", color=RED_COLOR),
                    view=None
                )
            if view.leve == 1:  

                m = await wait_for_msg(ctx, 60, msg)
                me = await commands.MemberConverter().convert(ctx=ctx, argument=m.content)
                if me.id in mod:
                  await ctx.reply(f"<@{me.id}> is already a Mod")
                else: 
                  g["mod"].append(me.id)
                  updateConfig(ctx.guild.id, g)                  
                  await ctx.reply(f"<@{me.id}> Has Been Made a Mod")

            elif view.leve == 2:
                m = await wait_for_msg(ctx, 60, msg)
                me = await commands.MemberConverter().convert(ctx=ctx, argument=m.content)
                if me.id not in mod:
                  await ctx.reply(f"<@{me.id}> is not a Mod")
                else: 
                  g["mod"].remove(me.id)
                  updateConfig(ctx.guild.id, g)  
                  await ctx.reply(f"<@{me.id}> Has Been Removed From Mod")

            elif view.leve == 3:
                result = ' '
                for i in mod:
                  user2 = self.client.get_user(i)
                  if user2 == None:
                        user = 'Unable to Fetch Name'
                  else:
                        user = user2.mention
                  result += f"{user}: {i}\n"
                if mod == []:
                  return await ctx.send("There are no Mod in this server, do `>mod` to add a user of your choice as Mod")
                else:
                    embed = discord.Embed(title=f'Mod for {ctx.guild.name}', description=result,
                                          color=0x2F3136)
                    await ctx.send(embed=embed)      

    @commands.command(help="Add Admin Function", aliases=['aa'])
    @commands.cooldown(3, 30, commands.BucketType.user)
    @is_admin()
    async def admin(self, ctx, config=None, setting: Union[discord.Member, discord.Role, int, str] = None):
        g = getConfig(ctx.guild.id)
        admin = g["admin"]


        if config is None:


            view = ModAdd(context=ctx)
            msg = await ctx.reply(f"""
**Bot Admin**
- {EMOJIS['idle']} Admin.
Please select a option.
                                """, view=view)

            await view.wait()

            if view.cancelled:
                return await msg.edit(
                    content="",
                    embed=discord.Embed(title=f"{EMOJIS['tick_no']} Cancelled", color=RED_COLOR),
                    view=None
                )
            if view.leve == 1:  

                m = await wait_for_msg(ctx, 60, msg)
                me = await commands.MemberConverter().convert(ctx=ctx, argument=m.content)
                if me.id in admin:
                  await ctx.reply(f"<@{me.id}> is already a Admin")
                else: 
                  g["admin"].append(me.id)
                  updateConfig(ctx.guild.id, g)                  
                  await ctx.reply(f"<@{me.id}> Has Been Made a Admin")

            elif view.leve == 2:
                m = await wait_for_msg(ctx, 60, msg)
                me = await commands.MemberConverter().convert(ctx=ctx, argument=m.content)
                if me.id not in admin:
                  await ctx.reply(f"<@{me.id}> is not a Admin")
                else: 
                  g["admin"].remove(me.id)
                  updateConfig(ctx.guild.id, g)  
                  await ctx.reply(f"<@{me.id}> Has Been Removed From Admin")

            elif view.leve == 3:
                result = ' '
                for i in admin:
                  user2 = self.client.get_user(i)
                  if user2 == None:
                        user = 'Unable to Fetch Name'
                  else:
                        user = user2.mention
                  result += f"{user}: {i}\n"
                if admin == []:
                  return await ctx.send("There are no Admin in this server, do `>admin` to add a user of your choice as Admin")
                else:
                    embed = discord.Embed(title=f'Admin for {ctx.guild.name}', description=result,
                                          color=0x2F3136)
                    await ctx.send(embed=embed)       
  
def setup(client):
    client.add_cog(Setup(client))