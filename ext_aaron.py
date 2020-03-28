import aiohttp
import asyncio
import botdb
import discord
import json
import random
from discord.ext import commands

class Aaron(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hola(self, ctx):
    await ctx.send('HOLA!')

  @commands.command()
  async def dadjoke(self, ctx):
    url = 'https://icanhazdadjoke.com/'
    headers={"Accept": "application/json"}
    async with aiohttp.ClientSession(headers=headers) as session:
      raw_response = await session.get(url)
      response = await raw_response.json()
      embed=discord.Embed(\
        title="Dad says...", 
        description=response['joke'])
      embed.set_thumbnail(url="https://media1.fdncms.com/orlando/imager/via/u/slideshow/2332140/mr-rogersjpg")
      await ctx.send("", embed=embed)

def setup(bot):
  bot.remove_command("hola")
  bot.remove_command("dadjoke")
  bot.add_cog(Aaron(bot))
