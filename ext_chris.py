import discord
import botdb
import os, random
from discord.ext import commands

class Chris():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def summonmaster(self):
     await self.bot.say('mmmm~ you summoned the dungeon master~ heheheh... <@214472130627239946>')

  @commands.command()
  async def ping(self):
     await self.bot.say('PONG BITCH!')

  @commands.command()
  async def crazy(self):
    await self.bot.say('oh no~ theres nothing you can throw at me.. *you cant win against my kind of crazy~*')

  @commands.command()
  async def snap(self):
    possible_responses = [
      'JIMMY! IMMA GET THE MOB BOSS ON YOUR ASS!',
      'MELVIN! IMMA HACK YOUR ROUTER, BISH! UGUGUGUGUGUGUGUGUG',
      'JERRY! IMMA STUFF YO ASS WITH BEEEANNNSSS, YEAH',
      'JUDY! NOW GIVE ME MY FUKIN NEWPORTS BITCH!',
      'ALISTAIR! Get in the fucking Dungeon and prepare for the most pain you have ever felt~',
    ]
    await self.bot.say('hmm.. who shall I be today? >:D *snaps fingers* oh.. now im ' + random.choice(possible_responses))

#################
# Test Currency #
#################
  @commands.command(pass_context=True)
  async def bal(self, context):
    key = context.message.author.name + "_" + context.message.author.discriminator + "_money"
    doc = botdb.get(key, "currency")
    if doc:
      await self.bot.say(context.message.author.mention + " Has **$%s**" % doc['bal'])
    else:
      await self.bot.say("Account not found. Adding it. (type !bal again)")
      botdb.set(key, {'bal': 0}, "currency")

  @commands.command(pass_context=True)
  async def testaddbal(self, context):
    key = context.message.author.name + "_" + context.message.author.discriminator + "_money"
    money = botdb.get(key, "currency")
    money['bal'] += 150
    botdb.set(key, money, "currency")
    await self.bot.say("Adding **$150** to your account.")

  @commands.command(pass_context=True)
  async def resetbal(self, context):
    key = context.message.author.name + "_" + context.message.author.discriminator + "_money"
    botdb.set(key, {'bal': 0}, "currency")
    await self.bot.say("Account reset.")

def setup(bot):
  bot.add_cog(Chris(bot))
