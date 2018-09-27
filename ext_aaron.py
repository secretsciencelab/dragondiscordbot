import discord
from discord.ext import commands

class Aaron():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hola(self):
    await self.bot.say('HOLA!')

def setup(bot):
  bot.add_cog(Aaron(bot))
