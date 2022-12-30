import os
import discord
import pymongo
import aiohttp
import logging
import datetime
import requests
from discord.ext import commands, tasks
from utils.checks import getConfig, updateConfig
from discord.colour import Color

IGNORE = (
    985097344880082964,
    
)
emoji = "<:arrow:1009092510792040528>"

class anti(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.culprit = False

    async def logs(self, guild, user, data, logchannel):
		      emergency_embed = discord.Embed(title="<:mod:1009092593461760120>Anti Logs<:mod:1009092593461760120>", color=Color.green(), description=f"{emoji}User    :   {user}\n{emoji}Crime    :   {data}\n{emoji}Time    :   <t:{(int(datetime.datetime.now().timestamp()))}:f>")
		      await logchannel.send(embed=emergency_embed)  

    async def whitelist(self,guild,user,data):
            g = getConfig(guild.id)
            wl = g['whitelist']
            if user.id == guild.owner.id:
                return
            elif user.id == self.client.user.id:
                return  
            elif user.id in wl:
                return 
            else:
                level = g['Punishment']
                logchannel = self.client.get_channel(g['log_channel'])
                if level == 1:                    
                  await guild.ban(user,
                                   reason=data)
                  await self.logs(guild, user, data, logchannel)
                elif level == 2:
                  await guild.kick(user,
                                   reason=data)
                  await self.logs(guild, user, data, logchannel)
                elif level == 3: 
                  mem = guild.get_member(user.id)
                  await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=data)
                  await self.logs(guild, user, data, logchannel)
                  return
                else:
                  return  

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel) -> None:
        guild = channel.guild       
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.channel_create):
            user = entry.user 
            data = f"[Anti Channel Create Triggerd] by {user}"      
            await self.whitelist(guild,user,data)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel) -> None:
        guild = channel.guild       
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.channel_delete):
            user = entry.user 
            data = f"[Anti Channel Delete Triggerd] by {user}"                    
            await self.whitelist(guild,user,data) 

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after) -> None:
      guild = before.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.channel_update):
            user = entry.user 
            data = f"[Anti Channel Update Triggerd] by {user}"      
            await self.whitelist(guild,user,data)

    @commands.Cog.listener()
    async def on_member_join(self, member) -> None: 
      guild = member.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.bot_add):
            user = entry.user 
            if member.bot:
              data = f"[Anti Bot Triggerd] by {user}"      
              g = getConfig(guild.id)
              wl = g['whitelist']
              if user.id == guild.owner.id:
                return
              elif user.id == self.client.user.id:
                return  
              elif user.id in wl:
                return 
              else:
                level = g['Punishment']
                logchannel = self.client.get_channel(g['log_channel'])
                if level == 1:                    
                  await guild.ban(user,
                                   reason=data)
                  await guild.ban(member,reason = data)
                  await self.logs(guild, user, data, logchannel)
                elif level == 2:
                  await guild.kick(user,
                                   reason=data)
                  await guild.ban(member,reason = data)
                  await self.logs(guild, user, data, logchannel)
                elif level == 3: 
                  mem = guild.get_member(user.id)
                  await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=data)
                  await guild.ban(member,reason = data)
                  await self.logs(guild, user, data, logchannel)
                  return
                else:
                  return    
                

    @commands.Cog.listener()
    async def on_guild_update(self, before, after) -> None:   
      guild = before.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.guild_update):
            user = entry.user 
            data = f"[Anti Guild Update Triggerd] by {user}"     
            await self.whitelist(guild,user,data)
      
              
    @commands.Cog.listener()
    async def on_member_remove(self, member) -> None:
      guild = member.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.kick):
            user = entry.user 
            data = f"[Anti Kick Triggerd] by {user}"      
            await self.whitelist(guild,user,data) 
                  
      async for entry1 in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.member_prune):  
            user1 = entry1.user 
            data = f"[Anti Prune Triggerd] by {user}"      
            await self.whitelist(guild,user1,data)      
                  
      
            
                
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user) -> None:
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.ban):
            user = entry.user 
            data = f"[Anti Ban Triggerd] by {user}"      
            await self.whitelist(guild,user,data)              

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user) -> None:
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.unban):
            user = entry.user 
            data = f"[Anti Unban Triggerd] by {user}"      
            await self.whitelist(guild,user,data)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role) -> None:
      guild = role.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.role_create):
            user = entry.user 
            data = f"[Anti Role Create Triggerd] by {user}"      
            await self.whitelist(guild,user,data)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role) -> None:
      guild = role.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.role_delete):
            user = entry.user 
            data = f"[Anti Role Delete Triggerd] by {user}"      
            await self.whitelist(guild,user,data)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after) -> None:
      guild = before.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.role_update):
            user = entry.user 
            data = f"[Anti Role Update Triggerd] by {user}"      
            await self.whitelist(guild,user,data)

    @commands.Cog.listener()
    async def on_webhooks_update(self, channel) -> None:
      guild = channel.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.webhook_create):  
            user = entry.user 
            data = f"[Anti Webhook Triggerd] by {user}"      
            await self.whitelist(guild,user,data)      

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member,
                               after: discord.Member) -> None:
      guild = after.guild
      async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.member_role_update):  
            user = entry.user 
            data = f"[Anti Member Role Update Triggerd] by {user}"     
            for role in after.roles:
                  if role not in before.roles:
                    if role.permissions.administrator or role.permissions.manage_guild or role.permissions.kick_members or role.permissions.ban_members:      
                     await self.whitelist(guild,user,data)
                    else: 
                      return      
              
                                 

                  
      

def setup(client):
	client.add_cog(anti(client))