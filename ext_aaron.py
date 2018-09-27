import botdb
import discord
from discord.ext import commands

class Aaron():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hola(self):
    await self.bot.say('HOLA!')

  @commands.command()
  async def dbset(self, key, value):
    botdb.set(key, {'value': value}, "aaron")

  @commands.command()
  async def dbget(self, key):
    doc = botdb.get(key, "aaron")
    if doc:
      await self.bot.say("%s" % doc['value'])
    else:
      await self.bot.say("Not found")

def setup(bot):
  bot.add_cog(Aaron(bot))
