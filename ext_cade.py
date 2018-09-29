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
      
   @commands.command(pass_context=True)
      async def ignorante(ctx, user):
    """This function send a meme to an user.
    Args:
        ctx: Bot Context
        user: User to notify
    """
    await ctx.bot.say(f"{user} ¡Ignorante de la vida!")
    await ctx.bot.send_file(ctx.message.channel,
                            "bot/static/img/mariano_ignorante.jpg")

def setup(bot):
  bot.add_cog(Cade(bot))
