import discord
from discord.ext import commands

class Chris():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def summonmaster(self):
     await self.bot.say('mmmm~ you summoned the dungeon master~ heheheh... <@214472130627239946>')

  @commands.command()
  async def pingbitch(self):
     await self.bot.say('PONG BITCH!')

  @commands.command()
  async def crazy(self):
    await self.bot.say('oh no~ theres nothing you can throw at me.. *you cant win against my kind of crazy~*')

def setup(bot):
  bot.add_cog(Chris(bot))
