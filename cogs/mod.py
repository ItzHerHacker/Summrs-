
import discord
import re
import urllib

from discord.ext import commands
import emojis
from datetime import datetime
from re import search
from collections import Counter
from utils.message import wait_for_msg
import asyncio
from discord.colour import Color
import datetime
from typing import Optional, Union
from utils.checks import getConfig, updateConfig, is_mod, is_admin
from utils.views import Modv, Confirm
from utils.bot import EpicBot
from handler import SlashCommandOption, InteractionContext, slash_command

prefix = ">"
emoji = "<:arrow:1009092510792040528>"
      
class Mod(commands.Cog, description="Moderation Commands"):
    def __init__(self, client: EpicBot):
        self.client = client

    """Moderation commands"""  

    def help_custom(self):
		      emoji = '<:mod:1009092593461760120>'
		      label = "Moderation"
		      description = "All Commands Related To Moderation"
		      return emoji, label, description     

    def convert(self, time):
      pos = ["s","m","h","d"]

      time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

      unit = time[-1]

      if unit not in pos:
          return -1
      try:
          val = int(time[:-1])
      except:
          return -2


      return val * time_dict[unit]  

    @commands.command(name="ban",help="Ban System", aliases=['b', 'hackban'])
    @commands.cooldown(3, 30, commands.BucketType.user)
    @is_mod() 
    async def _ban(self, ctx, user: discord.User = None, *, reason="No Reason Provided"):
      if user is None:
        return await ctx.send(
                "Invalid Usage! Please enter a user to ban.\nCorrect Usage: `>ban @user [reason]`"
            )
    
      else:  
        view = Confirm(context=ctx)
        emergency_embed = discord.Embed(title="<:mod:1009092593461760120>**Advance Ban**<:mod:1009092593461760120>", color=Color.green(), description=f"{emoji}**User**    :   {user.mention}\n{emoji}**Crime**    :   {reason}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}\n{emoji}**DO YOU WANT TO BAN {user.mention}**").set_thumbnail(url=user.display_avatar.url)
        msg = await ctx.send(embed=emergency_embed ,view=view)
    # Wait for the View to stop listening for input...
        await view.wait()
        if view.value is None:
          await msg.delete()
          await ctx.reply("Time Out")
        elif view.value:
          emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Banned** <:mod:1009092593461760120>", color=Color.green(), description=f"{emoji}**User**    :   {user}\n{emoji}**Crime**    :   {reason}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=user.display_avatar.url)
          await ctx.guild.ban(user, reason=reason)
          await msg.edit(embed=emergency, view=None)
        else:
          await msg.delete()
          await ctx.reply("Canceled")

    @slash_command(
      help="Ban a Member",
      options=[SlashCommandOption(name='user', type=6, description="Select a member to ban", required=True), SlashCommandOption(name='reason', type=3, description="Reason", required= False)]
    )
    async def ban(self, ctx: Union[commands.Context, InteractionContext], user: discord.User = None, *, reason="No Reason Provided"): 
      g = getConfig(ctx.guild.id)
      mod = g['mod']
      admin = g['admin']
      if ctx.author == ctx.guild.owner or ctx.author.id in mod or ctx.author.id in admin:
        await ctx.guild.ban(user, reason=reason)
        emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Banned** <:mod:1009092593461760120>", color=Color.green(), description=f"{emoji}**User**    :   {user}\n{emoji}**Crime**    :   {reason}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=user.display_avatar.url)
        await ctx.reply(embed=emergency)
      else:
        await ctx.reply("<:arrow:1009092510792040528> Only Server Moderators/Admins/Owner Can Use this Command")      

    @commands.command(name="kick", help="Kick System", aliases=['k'])
    @commands.cooldown(3, 30, commands.BucketType.user)
    @is_mod()
    async def _kick(self, ctx, user: discord.User = None, *, reason="No Reason Provided"):
      if user is None:
        return await ctx.send(
                "Invalid Usage! Please enter a user to ban.\nCorrect Usage: `>kick @user [reason]`"
            )
    
      else:  
        view = Confirm(context=ctx)
        emergency_embed = discord.Embed(title="<:mod:1009092593461760120>**Advance Kick**<:mod:1009092593461760120>", color=Color.green(), description=f"{emoji}**User**    :   {user.mention}\n{emoji}**Crime**    :   {reason}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}\n{emoji}**DO YOU WANT TO KICK {user.mention}**").set_thumbnail(url=user.display_avatar.url)
        msg = await ctx.send(embed=emergency_embed ,view=view)
    # Wait for the View to stop listening for input...
        await view.wait()
        if view.value is None:
          await msg.delete()
          await ctx.reply("Time Out")
        elif view.value:
          emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Kicked** <:mod:1009092593461760120>", color=Color.green(), description=f"{emoji}**User**    :   {user}\n{emoji}**Crime**    :   {reason}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=user.display_avatar.url)
          await ctx.guild.kick(user, reason=reason)
          await msg.edit(embed=emergency, view=None)
        else:
          await msg.delete()
          await ctx.reply("Cancelled")

    @slash_command(
      help="Kick a Member",
      options=[SlashCommandOption(name='user', type=6, description="Select a member to Kick", required=True), SlashCommandOption(name='reason', type=3, description="Reason", required= False)]
    )
    async def kick(self, ctx: Union[commands.Context, InteractionContext], user: discord.User = None, *, reason="No Reason Provided"): 
      g = getConfig(ctx.guild.id)
      mod = g['mod']
      admin = g['admin']
      if ctx.author == ctx.guild.owner or ctx.author.id in mod or ctx.author.id in admin:
        emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Kicked** <:mod:1009092593461760120>", color=Color.green(), description=f"{emoji}**User**    :   {user}\n{emoji}**Crime**    :   {reason}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=user.display_avatar.url)
        await ctx.guild.kick(user, reason=reason)
        await ctx.reply(embed=emergency)
      else:
        await ctx.reply("<:arrow:1009092510792040528> Only Server Moderators/Admins/Owner Can Use this Command") 

    @commands.command(name="lock", help="Locks the channel")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @is_mod()
    @commands.has_permissions(manage_channels=True)
    async def _lock(self, ctx: Union[commands.Context, InteractionContext], channel: discord.TextChannel = None): 
        channel = channel or ctx.channel
        view = Confirm(context=ctx)
        emergency_embed = discord.Embed(title="<:mod:1009092593461760120>**Advance Lock**<:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}\n{emoji}**DO YOU WANT TO LOCK {channel.mention}**").set_thumbnail(url=self.client.user.display_avatar.url) 
        msg = await ctx.send(embed=emergency_embed ,view=view)
        await view.wait()
        if view.value is None:
          await msg.delete()
          await ctx.reply("Time Out")
        elif view.value:
          emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Locked** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
          overwrite = channel.overwrites_for(ctx.guild.default_role)
          overwrite.send_messages = False
          await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Locked By {ctx.author}")
          await msg.edit(embed=emergency, view=None)
        else:
          await msg.delete()
          await ctx.reply("Canceled")      

    @slash_command(
        help="Lock a Channel",
        options=[SlashCommandOption(name='channel', type=7, description="Select a Channel To Lock", required=True)]
    )
    async def lock(self, ctx: Union[commands.Context, InteractionContext], channel: discord.TextChannel = None): 
      g = getConfig(ctx.guild.id)
      mod = g['mod']
      admin = g['admin']
      if ctx.author == ctx.guild.owner or ctx.author.id in mod or ctx.author.id in admin:
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Locked By {ctx.author}")
        emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Locked** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
        await ctx.reply(embed=emergency)
      else:
        await ctx.reply("<:arrow:1009092510792040528> Only Server Moderators/Admins/Owner Can Use this Command")
              
      
  
    @commands.command(name="unlock", help="Unlocks the channel")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @is_mod()
    @commands.has_permissions(manage_channels=True)
    async def _unlock(self, ctx, channel: discord.TextChannel = None):         
        channel = channel or ctx.channel
        view = Confirm(context=ctx)
        emergency_embed = discord.Embed(title="<:mod:1009092593461760120>**Advance Unlock**<:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}\n{emoji}**DO YOU WANT TO UNLOCK {channel.mention}**").set_thumbnail(url=self.client.user.display_avatar.url) 
        msg = await ctx.send(embed=emergency_embed ,view=view)
        await view.wait()
        if view.value is None:
          await msg.delete()
          await ctx.reply("Time Out")
        elif view.value:
          emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Unlocked** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
          overwrite = channel.overwrites_for(ctx.guild.default_role)
          overwrite.send_messages = True
          await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Unlocked By {ctx.author}")
          await msg.edit(embed=emergency, view=None)
        else:
          await msg.delete()
          await ctx.reply("Canceled")        

    @slash_command(
        help="Unock a Channel",
        options=[SlashCommandOption(name='channel', type=7, description="Select a Channel To Unlock", required=True)]
    )
    async def unlock(self, ctx: Union[commands.Context, InteractionContext], channel: discord.TextChannel = None): 
      g = getConfig(ctx.guild.id)
      mod = g['mod']
      admin = g['admin']
      if ctx.author == ctx.guild.owner or ctx.author.id in mod or ctx.author.id in admin:
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Unlocked By {ctx.author}")
        emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Unlocked** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
        await ctx.reply(embed=emergency)  
      else:
        await ctx.reply("<:arrow:1009092510792040528> Only Server Moderators/Admins/Owner Can Use this Command")
  
  
    @commands.command(name="hide", help="Hides the channel")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @is_mod()
    @commands.has_permissions(manage_channels=True)
    async def _hide(self, ctx, channel: discord.TextChannel = None): 
        channel = channel or ctx.channel
        view = Confirm(context=ctx)
        emergency_embed = discord.Embed(title="<:mod:1009092593461760120>**Advance Hide**<:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}\n{emoji}**DO YOU WANT TO HIDE {channel.mention}**").set_thumbnail(url=self.client.user.display_avatar.url) 
        msg = await ctx.send(embed=emergency_embed ,view=view)
        await view.wait()
        if view.value is None:
          await msg.delete()
          await ctx.reply("Time Out")
        elif view.value:
          emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Hided** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
          overwrite = channel.overwrites_for(ctx.guild.default_role)
          overwrite.view_channel = False
          await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Hided By {ctx.author}")
          await msg.edit(embed=emergency, view=None)
        else:
          await msg.delete()
          await ctx.reply("Canceled")      

    @slash_command(
        help="Hide a Channel",
        options=[SlashCommandOption(name='channel', type=7, description="Select a Channel To Hide", required=True)]
    )
    async def hide(self, ctx: Union[commands.Context, InteractionContext], channel: discord.TextChannel = None): 
      g = getConfig(ctx.guild.id)
      mod = g['mod']
      admin = g['admin']
      if ctx.author == ctx.guild.owner or ctx.author.id in mod or ctx.author.id in admin:
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = False
        await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Hided By {ctx.author}")
        emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Hided** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
        await ctx.reply(embed=emergency)
      else:
        await ctx.reply("<:arrow:1009092510792040528> Only Server Moderators/Admins/Owner Can Use this Command")  
  
    @commands.command(name="unhide", help="Unhides the channel")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @is_mod()
    @commands.has_permissions(manage_channels=True)
    async def _unhide(self, ctx, channel: discord.TextChannel = None):        
        channel = channel or ctx.channel
        view = Confirm(context=ctx)
        emergency_embed = discord.Embed(title="<:mod:1009092593461760120>**Advance Unhide**<:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}\n{emoji}**DO YOU WANT TO UNHIDE {channel.mention}**").set_thumbnail(url=self.client.user.display_avatar.url) 
        msg = await ctx.send(embed=emergency_embed ,view=view)
        await view.wait()
        if view.value is None:
          await msg.delete()
          await ctx.reply("Time Out")
        elif view.value:
          emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Unhided** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
          overwrite = channel.overwrites_for(ctx.guild.default_role)
          overwrite.view_channel = True
          await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Unhided By {ctx.author}")
          await msg.edit(embed=emergency, view=None)
        else:
          await msg.delete()
          await ctx.reply("Canceled")       

    @slash_command(
        help="Unhide a Channel",
        options=[SlashCommandOption(name='channel', type=7, description="Select a Channel To Unhide", required=True)]
    )
    async def unhide(self, ctx: Union[commands.Context, InteractionContext], channel: discord.TextChannel = None): 
      g = getConfig(ctx.guild.id)
      mod = g['mod']
      admin = g['admin']
      if ctx.author == ctx.guild.owner or ctx.author.id in mod or ctx.author.id in admin:
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = True
        await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Unhided By {ctx.author}")
        emergency = discord.Embed(title="<:mod:1009092593461760120>**Sucessfully Unhided** <:mod:1009092593461760120>", color=0x2F3136, description=f"{emoji}**Channel**    :   {channel.mention}\n{emoji}**Time**    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>\n{emoji}**Moderator**    :   {ctx.author.mention}").set_thumbnail(url=self.client.user.display_avatar.url)
        await ctx.reply(embed=emergency)
      else:
        await ctx.reply("<:arrow:1009092510792040528> Only Server Moderators/Admins/Owner Can Use this Command")   
  

def setup(client):
    client.add_cog(Mod(client))