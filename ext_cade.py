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
      
def hello_function(message,client,args):
    try:
        return 'Hello {}, Argument One: {}'.format(message.author, args[0])
    except Exception as e:
        return e

# hello command dictionary
hello_command = {
    # if the string starts with this the function will be called
    'trigger': '!hello',
    
    # specifies the function to call
    'function': hello_function,
    
    # number of arguments that the functions needs
    'args_num': 1,
    
    # name of the argument that the funtions takes
    'args_name': ['string'],
    
    # describes what the function does
    'description': 'Will respond hello to the caller and show arg 1'
}

def setup(bot):
  bot.add_cog(Cade(bot))
