import discord
from discord.ext import commands

class Chris():
  def __init__(self, bot):
    self.bot = bot

@commands.command()
async def summonmaster(self):
    await self.bot.say('mmmm~ you summoned the dungeon master~ heheheh... ' + <@214472130627239946>)

@commands.command()
async def ping(self):
    await self.bot.say('PONG BITCH!')

def setup(bot):
  bot.add_cog(Chris(bot))
