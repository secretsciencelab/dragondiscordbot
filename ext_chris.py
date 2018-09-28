import discord
import datetime
import botdb
import os, random
from random import randint
from discord import Game
from discord.ext import commands

class Chris():
  def __init__(self, bot):
    self.bot = bot

##################
# Random/Testing #
##################
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
# Informational #
#################
  @commands.command()
  async def chrishelp(self):
    embed=discord.Embed(title="Chris Module Help (CMD Prefix: '!' or '$')", description="Available commands in this Personality Module", color=0x3e0913)
    embed.add_field(name="Random/Test CMDs", value="""
                      **ping** - Test Command
                      **summonmaster** - If you wish to summon Chris
                      **crazy** - Think you can throw anything at Chris?
                      **snap** - Go into character~""")
    embed.add_field(name="Currency/Gambling CMDs", value="""
                      **bal** - Check your balance
                      **daily** - Get a daily reward
                      **slots** - If you wish to play slots""")
    await self.bot.say("", embed=embed)


############
# Currency #
############
  @commands.command(pass_context=True)
  async def bal(self, context):
    name=""
    desc=""
    key = context.message.author.name + "_" + context.message.author.discriminator + "_money"
    doc = botdb.get(key, "currency")
    if doc:
      name=context.message.author.name + "'s Currency card"
      desc="Card No/ID: **" + context.message.author.id + "**\nYou have **$%s**" % doc['bal']
    else:
      name="Error"
      desc="Account not found. Adding it. (type !bal again)"
      botdb.set(key, {'bal': 1000}, "currency")

    embed=discord.Embed(title="DragonScript Bank", description="User Balance Info", color=0x1abc9c)
    embed.set_thumbnail(url=context.message.author.avatar_url)
    embed.add_field(name=name, value=desc)
    await self.bot.say(context.message.author.mention, embed=embed)

#  @commands.command(pass_context=True)
#  async def testaddbal(self, context):
#    key = context.message.author.name + "_" + context.message.author.discriminator + "_money"
#    money = botdb.get(key, "currency")
#    money['bal'] += 150
#    botdb.set(key, money, "currency")
#    embed=discord.Embed(title="DragonScript Bank", description="User Balance Info", color=0x1abc9c)
#    embed.set_thumbnail(url=context.message.author.avatar_url)
#    embed.add_field(name=context.message.author.name + "'s Currency card", value="Card No/ID: **" + context.message.author.id + "**\nAdding **$150** to your account.")
#    await self.bot.say(context.message.author.mention, embed=embed)

  @commands.command(pass_context=True)
  async def daily(self, context):
    dailykey = context.message.author.name + "_" + context.message.author.discriminator + "_dailyuse"
    moneykey = context.message.author.name + "_" + context.message.author.discriminator + "_money"
    dblastdailyuse = botdb.get(dailykey, "daily")
    money = botdb.get(moneykey, "currency")
    currentday=datetime.datetime.now().day

    if money == None:
      botdb.set(moneykey, 1000, "currency")

    if dblastdailyuse == None:
      # First ever daily
      botdb.set(dailykey, {'lastdailyuse': currentday}, "daily")
      money['bal'] += 700
      botdb.set(moneykey, money, "currency")
      embed=discord.Embed(title="DragonScript Bank [DAILY]", description="User Balance Info", color=0xecff00)
      embed.set_thumbnail(url=context.message.author.avatar_url)
      embed.add_field(name=context.message.author.name + "'s Currency card", value="Card No/ID: **" + context.message.author.id + "**\nDaily reward of **$500** with a First Time Bonus of **+$200** received.")
      await self.bot.say(context.message.author.mention, embed=embed)
      return

    if dblastdailyuse['lastdailyuse'] != currentday:
      # After first ever daily
      botdb.set(dailykey, {'lastdailyuse': currentday}, "daily")
      money['bal'] += 500
      botdb.set(moneykey, money, "currency")
      embed=discord.Embed(title="DragonScript Bank [DAILY]", description="User Balance Info", color=0xecff00)
      embed.set_thumbnail(url=context.message.author.avatar_url)
      embed.add_field(name=context.message.author.name + "'s Currency card", value="Card No/ID: **" + context.message.author.id + "**\nDaily reward of **$500** received.")
      await self.bot.say(context.message.author.mention, embed=embed)
      return
    elif dblastdailyuse['lastdailyuse'] == currentday:
      eremb=discord.Embed(title="DragonScript Bank [ERROR]", description="You cannot use your Daily again today. (Last day of use: **" + dblastdailyuse['lastdailyuse'].__str__() + "**)", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return


  @commands.command(pass_context=True)
  async def steal(self, context, target : discord.User = None):
    laststolenfromkey = "laststolenfrom_key"
    lastuserstolenfrom = botdb.get(laststolenfromkey, "stealing")
    if target == None:
      eremb=discord.Embed(title="Stealing [ERROR]", description="Please specify a user! (ex: !steal @Steel_Dev#3344)", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return
    else:
      if target == context.message.author:
        eremb=discord.Embed(title="Stealing [ERROR]", description="You cannot steal from yourself. Ya idjit", color=0xFF0000)
        await self.bot.say(context.message.author.mention, embed=eremb)
        return   

      if lastuserstolenfrom == None:
        botdb.set(laststolenfromkey, {'laststolenfrom': context.message.author.name}, "stealing")
        lastuserstolenfrom = botdb.get(laststolenfromkey, "stealing")

      if target.name == lastuserstolenfrom['laststolenfrom'] and lastuserstolenfrom != None:
        eremb=discord.Embed(title="Stealing [ERROR]", description="This user has already been stolen from last. try someone else.", color=0xFF0000)
        await self.bot.say(context.message.author.mention, embed=eremb)
        return

      cmdrunnermoneykey = context.message.author.name + "_" + context.message.author.discriminator + "_money"
      targetmoneykey = target.name + "_" + context.message.author.discriminator + "_money"
      cmdrunnermoney = botdb.get(cmdrunnermoneykey, "currency")
      targetmoney = botdb.get(targetmoneykey, "currency")

      randstealam = randint(150, 250)

      if cmdrunnermoney == None:
        botdb.set(cmdrunnermoneykey, {'bal': 1000}, "currency")

      if targetmoney == None:
        botdb.set(targetmoneykey, {'bal': 1000}, "currency")

      if cmdrunnermoney['bal'] <= 100:
        randstealam = randstealam/2

      if targetmoney['bal'] >= randstealam:
        randchance = randint(0, 3)
        if randchance == 2:
          targetmoney['bal'] -= randstealam
          botdb.set(targetmoneykey, {'bal': targetmoney}, "currency")
          botdb.set(laststolenfromkey, {'laststolenfrom': target.name}, "stealing")
          eremb=discord.Embed(title="Stealing [SUCCESS!]", description="Successfully stolen **$" + randstealam.__str__() + "** from " + target.name + "!", color=0xecff00)
          await self.bot.say(target.mention, embed=eremb)
        else:
          lost=""
          if cmdrunnermoney['bal'] >= 50:
            cmdrunnermoney['bal'] -= 50
            targetmoney['bal'] += 50
            botdb.set(cmdrunnermoneykey, {'bal': cmdrunnermoney}, "currency")
            botdb.set(targetmoneykey, {'bal': targetmoney}, "currency")
            lost="You lost **$50** when running away!"
          eremb=discord.Embed(title="Stealing [FAILED!]", description="Failed to steal from " + target.name + "! " + lost, color=0xFF0000)
          await self.bot.say(context.message.author.mention, embed=eremb)

# Slots emotes; :spades: :clubs: :hearts: :diamonds: :dragon: 
############
# Gambling #
############
# Work on chances- make it a little easier to win
  @commands.command(pass_context=True)
  async def slots(self, context, am : int = 0):
    key = context.message.author.name + "_" + context.message.author.discriminator + "_money"
    doc = botdb.get(key, "currency")

    if am == 0:
      eremb=discord.Embed(title="DragonBot Slots [ERROR]", description="Please place a bet. (ex: !slots 100)", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return 
    if am < 50:
      eremb=discord.Embed(title="DragonBot Slots [ERROR]", description="You cannot bet any lower than **$50**", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return    
    if am > 500:
      eremb=discord.Embed(title="DragonBot Slots [ERROR]", description="You cannot bet any higher than **$500**", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return        

    spadesvalue=am*4
    clubsvalue=am*5
    heartsvalue=am*6
    diamondsvalue=am*7
    dragonsvalue=am*9 # Jackpot

    slot1=""
    slot2=""
    slot3=""

    result=""

    rescol=0x1abc9c

    possible_slots = [
      ':spades:',
      ':clubs:',
      ':hearts:',
      ':diamonds:',
      ':dragon:',
      ':clubs:',
      ':spades:',
      ':dragon:',
      ':clubs:',
      ':spades:',
      ':hearts:',
      ':clubs:',
      ':hearts:',
      ':clubs:',
      ':hearts:',
      ':diamonds:',
      ':hearts:',
      ':clubs:',
      ':hearts:',
      ':diamonds:',
      ':clubs:',
      ':hearts:',
      ':diamonds:',
      ':dragon:',
      ':spades:',
      ':diamonds:',
      ':dragon:',
      ':spades:',
      ':diamonds:',
      ':clubs:',
      ':hearts:',
      ':diamonds:',
      ':clubs:',
      ':hearts:',
      ':diamonds:',
      ':spades:',
      ':hearts:',
      ':dragon:',
    ]

    slot1=random.choice(possible_slots)
    slot2=random.choice(possible_slots)
    slot3=random.choice(possible_slots)

    money = botdb.get(key, "currency")


    if doc['bal'] >= am:
      money['bal'] -= am
      botdb.set(key, money, "currency")

      if slot1 == possible_slots[0] and slot2 == possible_slots[0] and slot3 == possible_slots[0]:
        # won 1 slot
        rescol=0x32e00f
        money['bal'] += spadesvalue
        botdb.set(key, money, "currency")
        result="Winner! You won **$" + spadesvalue.__str__() + "**!"
      elif slot1 == possible_slots[1] and slot2 == possible_slots[1] and slot3 == possible_slots[1]:
        # won 2 slot
        rescol=0x32e00f
        money['bal'] += clubsvalue
        botdb.set(key, money, "currency")
        result="Winner! You won **$" + clubsvalue.__str__() + "**!"
      elif slot1 == possible_slots[2] and slot2 == possible_slots[2] and slot3 == possible_slots[2]:
        # won 3 slot
        rescol=0x32e00f
        money['bal'] += heartsvalue
        botdb.set(key, money, "currency")
        result="Winner! You won **$" + heartsvalue.__str__() + "**!"
      elif slot1 == possible_slots[3] and slot2 == possible_slots[3] and slot3 == possible_slots[3]:
        # won 4 slot
        rescol=0x32e00f
        money['bal'] += diamondsvalue
        botdb.set(key, money, "currency")
        result="Winner! You won **$" + diamondsvalue.__str__() + "**!"
      elif slot1 == possible_slots[4] and slot2 == possible_slots[4] and slot3 == possible_slots[4]:
        # won 5 slot -- jackpot
        rescol=0xecff00
        money['bal'] += dragonsvalue
        botdb.set(key, money, "currency")
        result="JACKPOT!! You won **$" + dragonsvalue.__str__() + "**!"
      else:
        rescol=0xFF0000
        result="BUST! You won nothing! You lost **$" + am.__str__() + "**!"
    else:
      eremb=discord.Embed(title="DragonBot Slots [ERROR]", description="You need at least **$50** or more to use slots.", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return
    slotsemb=discord.Embed(title="DragonScript Slots", description="You bet **$" + am.__str__() + "** and..", color=rescol)
    slotsemb.add_field(name="Result", value=slot1 + " | " + slot2 + " | " + slot3)
    slotsemb.add_field(name="Rewards", value=":spades: - **$" + spadesvalue.__str__() + "**\n:clubs: - **$" + clubsvalue.__str__() + "**\n:hearts: - **$" + heartsvalue.__str__() + "**\n:diamonds: - **$" + diamondsvalue.__str__() + "**\n:dragon: - **JACKPOT $" + dragonsvalue.__str__() + "**")
    slotsemb.add_field(name="And..", value=result, inline=False)
    await self.bot.say(context.message.author.mention, embed=slotsemb)

def setup(bot):
  bot.add_cog(Chris(bot))
