import discord
from discord.ext import commands

class kami():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def owo():
    await self.bot.say("What's this?")

  @commands.command()
  asyn def joker():
    await self.bot.say("Looking cool Joker!")

def setup(bot):
  bot.add_cog(Kami(bot))
