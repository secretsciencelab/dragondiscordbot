import aiohttp
import asyncio
import botdb
import discord
import json
import random
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

  @commands.command()
  async def chuck(self):
    url = 'https://api.chucknorris.io/jokes/random'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
      raw_response = await session.get(url)
      response = await raw_response.text()
      response = json.loads(response)
      embed=discord.Embed(title="Chuck Norris Fact", description="")
      #embed.set_thumbnail(url=response['icon_url'])
      embed.set_thumbnail(url="https://images02.military.com/sites/default/files/styles/full/public/media/veteran-jobs/content-images/2016/03/chucknorris.jpg?itok=_J3M4O-S")
      embed.add_field(name="", value=response['value'])
      await self.bot.say("", embed=embed)

def setup(bot):
  bot.add_cog(Aaron(bot))
