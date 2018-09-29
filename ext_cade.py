import botdb
import discord
from discord.ext import commands

class Cade():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def Help(self):
    await self.bot.say('I feel dead inside :D')

  @commands.command()
  async def dbset(self, key, value):
    botdb.set(key, {'value': value}, "cade")

  @commands.command()
  async def dbget(self, key):
    doc = botdb.get(key, "cade")
    if doc:
      await self.bot.say("%s" % doc['value'])
    else:
      await self.bot.say("Not found")
      
      foo = input("Enter a Number: ")
      
      print(foo)
      
def setup(bot):
  bot.add_cog(Cade(bot))
