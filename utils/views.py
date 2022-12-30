import discord
from discord.ext import commands
from typing import Optional, Union



class Confirm(discord.ui.View):
    def __init__(self, context):
        super().__init__(timeout=None)
        self.level = 0
        self.context = context
        self.value = None


    @discord.ui.button(label='Yes', style=discord.ButtonStyle.green)
    async def next(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user != self.context.author:
            return await interaction.response.send_message("You cannot interact in someone else's interaction.", ephemeral=True)
        else:
          self.value = True
          self.stop()

          
    @discord.ui.button(label='No', style=discord.ButtonStyle.red)
    async def cancel(self, b: discord.ui.Button, i: discord.Interaction):
        if i.user != self.context.author:
            return await i.response.send_message("You cannot interact in someone else's interaction.", ephemeral=True)
        else:   
          self.value = False
          self.stop()

   

class Modv(discord.ui.View):
    def __init__(self, context):
        super().__init__(timeout=None)
        self.value = 0
        self.context = context

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Ban', style=discord.ButtonStyle.red)
    async def bans(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='kick', style=discord.ButtonStyle.red)
    async def kicks(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()

    @discord.ui.button(label='Mute', style=discord.ButtonStyle.red)
    async def mutes(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop() 

    @discord.ui.button(label='Unmute', style=discord.ButtonStyle.green)
    async def unmutes(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 4
        self.stop()  

    @discord.ui.button(label='Unban', style=discord.ButtonStyle.green)
    async def unbans(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 5
        self.stop()   
