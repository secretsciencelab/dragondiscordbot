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
    async with aiohttp.ClientSession() as session:
      raw_response = await session.get(url)
      response = await raw_response.text()
      response = json.loads(response)
      randomNum = random.randint(1,1000)
      embed=discord.Embed(\
        title="Chuck Norris Fact #%d" % randomNum, 
        description=response['value'])
      #embed.set_thumbnail(url=response['icon_url'])
      embed.set_thumbnail(url="https://files.sharenator.com/chuck_100_Chuck_Norris_Facts-s390x300-11888.jpg")
      await self.bot.say("", embed=embed)

  @commands.command()
  async def dadjoke(self):
    url = 'https://icanhazdadjoke.com/'
    headers={"Accept": "application/json"}
    async with aiohttp.ClientSession(headers=headers) as session:
      raw_response = await session.get(url)
      response = await raw_response.json()
      embed=discord.Embed(\
        title="Dad says..", 
        description=response['joke'])
      embed.set_thumbnail(url="https://media1.fdncms.com/orlando/imager/via/u/slideshow/2332140/mr-rogersjpg")
      await self.bot.say("", embed=embed)

def setup(bot):
  bot.add_cog(Aaron(bot))
