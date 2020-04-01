import aiohttp
import asyncio
import botdb
import discord
import json
import random
from discord.ext import commands

class Dragondrawer(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def drawadragon(self, ctx):
    await ctx.send('https://i.ytimg.com/vi/Iqr_yP25wug/maxresdefault.jpg') 
    
  @commands.command()
  async def babyyoda(self, ctx):
    await ctx.send('A wholesome meme...https://media1.tenor.com/images/42ee9b64cad9d525e2fcea4530b4200f/tenor.gif?itemid=15914167')
    
  @commands.command()
  async def pKIRBY(self, ctx):
    await ctx.send("Desc: NONE https://cdn.discordapp.com/attachments/691091650797240360/694733357551976488/sshot-049.png")

def setup(bot):
  bot.remove_command("drawadragon")
  bot.remove_command("babyyoda")
  bot.remove_command("pKIRBY")
  bot.add_cog(Dragondrawer(bot))
