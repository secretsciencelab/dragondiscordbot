import discord
import random
from discord.ext import commands

class Dragondrawer():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def Drawadragon(self):
    await self.ctx.send("https://i.ytimg.com/vi/Iqr_yP25wug/maxresdefault.jpg")
    
  @commands.command()
  async def babyyoda(self):
    await self.ctx.send("A wholesome meme...https://media1.tenor.com/images/42ee9b64cad9d525e2fcea4530b4200f/tenor.gif?itemid=15914167")
    
  @commands.command()
  async def pK I R B Y(self):
    await self.ctx.send("Desc: https://cdn.discordapp.com/attachments/691091650797240360/694733357551976488/sshot-049.png")

def setup(bot):
  bot.add_cog(Dragondrawer(bot))
https://cdn.discordapp.com/attachments/691091650797240360/694733357551976488/sshot-049.png
