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
  async def RBLXservers(self, ctx):
    await ctx.send('Unofficial DSA Roblox Game warp: https://sites.google.com/view/dsa-roblox-warp/home')
    
  @commands.command()
  async def pKIRBY(self, ctx):
    await ctx.send("Desc: kirby is 8 inches tall 28 yrs old roles: NONE https://cdn.discordapp.com/attachments/691091650797240360/694733357551976488/sshot-049.png")

  @commands.command()
  async def pSuccosis(self, ctx):
    await ctx.send("Desc: NONE roles: Dragonbot developer, DragonScripter https://cdn.discordapp.com/attachments/471445210904264757/693657259049222240/sshot-044.png")
        
  @commands.command()
  async def pSteel(self, ctx):
    await ctx.send("Desc: NONE roles: Dragonbot Developer, DragonScripter, team, DragonScript Champion, $ https://cdn.discordapp.com/attachments/471445210904264757/693667947964661830/sshot-046.pngg")
    
  @commands.command()
  async def pkami64(self, ctx):
    await ctx.send("Desc: NONE roles: Dragonbot Developer, $ https://cdn.discordapp.com/attachments/691091650797240360/695058854190514276/sshot-052.png")
    
def setup(bot):
  bot.remove_command("drawadragon")
  bot.remove_command("babyyoda")
  bot.remove_command("pKIRBY")
  bot.remove_command("pSuccosis")
  bot.remove_command("pSteel")
  bot.remove_command("pkami64")
  bot.add_cog(Dragondrawer(bot))

  
