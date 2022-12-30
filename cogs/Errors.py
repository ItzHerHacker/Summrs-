import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CommandNotFound, BotMissingPermissions, MissingRequiredArgument, CheckFailure


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        prefix = ">"
        if isinstance(error, commands.CommandOnCooldown):
            minute = round(error.retry_after)
            if minute > 0:
                await ctx.send("Command Cooldown: {0} second(s)!".format(minute))

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Wrong Usage",
                                  description=f"`{prefix}{ctx.command.name} {ctx.command.usage}`", colour=0x2F3136)
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            emote = ("<:arrow:1009092510792040528>")
            await ctx.send(f"{emote} You must have a higher role to use this command")

        if isinstance(error, commands.MemberNotFound):
            emote = ("<:arrow:1009092510792040528>")
            await ctx.send(f"{emote} Member not found")

        if isinstance(error, commands.RoleNotFound):
            emote = ("<:arrow:1009092510792040528>")
            await ctx.send(f"{emote} Role not found")

        if isinstance(error, commands.BotMissingPermissions):
            emote = ("<:arrow:1009092510792040528>")
            await ctx.send(f"{emote} Missing some important permissions, check if Server Security has the administrator permission ")

        if isinstance(error, commands.CheckFailure):
            emote = ("<:arrow:1009092510792040528>")
            await ctx.send(f"{emote} Only Server Moderators/Admins/Owner Can Use this Command")  






def setup(client):
    client.add_cog(Errors(client))