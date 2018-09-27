import discord
from discord.ext import commands

class Aaron():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(self):
    await self.bot.say('pong')

def setup(bot):
  bot.add_cog(Aaron(bot))
