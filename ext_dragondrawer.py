import discord
import random
from discord.ext import commands

class Dragondrawer():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def Drawadragon(self):
    await self.bot.say("https://i.ytimg.com/vi/Iqr_yP25wug/maxresdefault.jpg")
    
  @commands.command()
  async def babyyoda(self):
    await self.bot.say("A wholesome meme...https://media1.tenor.com/images/42ee9b64cad9d525e2fcea4530b4200f/tenor.gif?itemid=15914167")

def setup(bot):
  bot.add_cog(Dragondrawer(bot))
