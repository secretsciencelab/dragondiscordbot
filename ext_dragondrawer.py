import discord
import random
from discord.ext import commands

class Dragondrawer():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def Drawadragon(self):
    await self.bot.say("https://i.ytimg.com/vi/Iqr_yP25wug/maxresdefault.jpg")

def setup(bot):
  bot.add_cog(Dragondrawer(bot))
