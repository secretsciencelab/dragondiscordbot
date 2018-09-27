import discord
from discord.ext import commands

class Chris():
  def __init__(self, bot):
    self.bot = bot
    self.bot.say('mmmm~ you summoned the dungeon master~ heheheh...')

  @commands.command()
  async def ping(self):
    await self.bot.say('PONG BITCH!')

def setup(bot):
  bot.add_cog(Chris(bot))
