import discord
import datetime
import botdb
import os, random
from random import randint
from discord import Game
from discord.ext import commands

# Class
class Chris():

  # Initialization
  def __init__(self, bot):
    self.bot = bot

##################
# Random/Testing #
##################

# Summon the master - Random command
  @commands.command()
  async def summonmaster(self):
     await self.bot.say('mmmm~ you summoned the dungeon master~ heheheh... <@214472130627239946>')

# Ping - Random test command
  @commands.command()
  async def ping(self):
     await self.bot.say('PONG BITCH!')

# Craziness - Random command
  @commands.command()
  async def crazy(self):
    await self.bot.say('oh no~ theres nothing you can throw at me.. *you cant win against my kind of crazy~*')

# Snap - Random command
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

# Lick - Random command
  @commands.command()
  async def lick(self, target : discord.User):
      possible_responses = [
          'Oh god.. you taste like crusty anal..',
          'OH JESUS WHY, SHOWER! SHOWER!',
          '*pukes* o-oh jeez.. oh god.. why',
          'MMMMMMMMMMMMM ANAL! you gross fuck..',
          'Definitely swam in a septic tank..',
          'YOU TASTE LIKE ROTTEN DICK! EW EW!',
          'OH JESUS, DID YOU HAVE A HOOKER GIVE YOU A CLEVELAND STEAMER?!',
          'You taste like a baby after its been FUCKED! (godkillmenowwhydoidothethingsido)'
      ]
      await self.bot.say("*licks " + target.mention + "*    .." + random.choice(possible_responses))

# Lyrics - Random command
  @commands.command(pass_context=True)
  async def lyrics(self, context):
    lyric_list=[
      'We set the fires to take us higher, we set the fires to watch them fucking ***BURN.. BURN, BURN, BURN BURN BURN!***',
      'Im haunted by my wildest dreams, im haunted by the darkness inside me',
      'Emptiness is filling me, to the point of agony, growing darkness taking dawn.. I was me *but now hes gone*',
      'Take a look, to the sky, just before you die, *its the last time you will!*'
    ]
    chosenlyric=random.choice(lyric_list)
    await self.bot.say(context.message.author.mention + "   " + chosenlyric)

#################
# Informational #
#################

# Help - Information command
  @commands.command()
  async def chrishelp(self):
    embed=discord.Embed(title="Chris Module Help (CMD Prefix: '!' or '$')", description="Available commands in this Personality Module", color=0x3e0913)
    embed.add_field(name="Random/Test CMDs", value="""
                      **ping** - Test Command
                      **summonmaster** - If you wish to summon Chris
                      **crazy** - Think you can throw anything at Chris?
                      **snap** - Go into character~
                      **lick** - Lick anyone you want!""")
    embed.add_field(name="Currency/Gambling CMDs", value="""
                      **bal** - Check your balance
                      **daily** - Get a daily reward
                      **slots** - If you wish to play slots
                      **roulette** - Are you lucky enough?
                      **steal** - Wanna be a cunt? go ahead""")
    embed.add_field(name="Admin CMDs", value="""
                    **abal** - Manage any users balance""")
    await self.bot.say("", embed=embed)

############
# Currency #
############

# Balance - Check any users balance command
  @commands.command(pass_context=True)
  async def bal(self, context, target : discord.User = None):
    name=""
    desc=""

    if target == None:
      target = context.message.author

    if target == self.bot.user:
      eremb=discord.Embed(title="Stealing [ERROR]", description="Bots cannot have money.", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return    

    key = target.name + "_" + target.discriminator + "_money"
    doc = botdb.get(key, "currency")

    if doc:
      if doc['bal'] < 0:
        botdb.set(key, {'bal': 0}, "currency")
        doc = botdb.get(key, "currency")

      name=target.name + "'s Currency card"
      desc="Card No/ID: **" + target.id + "**\n" + target.name + " has: **$%s**" % doc['bal']
    else:
      name="Error"
      desc="Account not found. Adding it. (type !bal again)"
      botdb.set(key, {'bal': 1000}, "currency")

    embed=discord.Embed(title="DragonScript Bank", description="User Balance Info", color=0x1abc9c)
    embed.set_thumbnail(url=target.avatar_url)
    embed.add_field(name=name, value=desc)
    await self.bot.say(context.message.author.mention, embed=embed)

# Daily - Get your daily reward command
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

# Steal - Steal from any user command
  @commands.command(pass_context=True)
  @commands.cooldown(1, 35, commands.BucketType.user)
  async def steal(self, context, target : discord.User = None):
    laststolenfromkey = "laststolenfrom_key"
    lastuserstolenfrom = botdb.get(laststolenfromkey, "stealing")

    if target == self.bot.user:
      eremb=discord.Embed(title="Stealing [ERROR]", description="Can't steal from bots.", color=0xFF0000)
      await self.bot.say(context.message.author.mention, embed=eremb)
      return      

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

      if target.name == lastuserstolenfrom['laststolenfrom'].__str__() and lastuserstolenfrom != None:
        eremb=discord.Embed(title="Stealing [ERROR]", description="This user has already been stolen from last. try someone else.", color=0xFF0000)
        await self.bot.say(context.message.author.mention, embed=eremb)
        return

      cmdrunnermoneykey = context.message.author.name + "_" + context.message.author.discriminator + "_money"
      targetmoneykey = target.name + "_" + target.discriminator + "_money"

      cmdrunnermoney = botdb.get(cmdrunnermoneykey, "currency")
      targetmoney = botdb.get(targetmoneykey, "currency")

      if cmdrunnermoney == None:
        botdb.set(cmdrunnermoneykey, {'bal': 1000}, "currency")
        cmdrunnermoney = botdb.get(cmdrunnermoneykey, "currency")

      if targetmoney == None:
        botdb.set(targetmoneykey, {'bal': 1000}, "currency")
        targetmoney = botdb.get(targetmoneykey, "currency")

      amountstealing = 1000

      if cmdrunnermoney['bal'] <= 100:
        amountstealing = 75

      if targetmoney['bal'] < amountstealing:
          eremb=discord.Embed(title="Stealing [ERROR!]", description=target.name + " Doesn't have enough. Pick on someone who isn't broke off their ass.", color=0xFF0000)
          await self.bot.say(context.message.author.mention, embed=eremb)
          return

      if targetmoney['bal'] >= amountstealing:
        randchance = randint(0, 1)
        if randchance == 1:
          targetmoney['bal'] -= amountstealing
          cmdrunnermoney['bal'] += amountstealing
          botdb.set(cmdrunnermoneykey, cmdrunnermoney, "currency")
          botdb.set(targetmoneykey, targetmoney, "currency")
          botdb.set(laststolenfromkey, {'laststolenfrom': target.name}, "stealing")
          eremb=discord.Embed(title="Stealing [SUCCESS!]", description="Successfully stolen **$" + amountstealing.__str__() + "** from " + target.name + "!", color=0xecff00)
          await self.bot.say(target.mention, embed=eremb)
        else:
          lost=""
          if cmdrunnermoney['bal'] >= 50:
            cmdrunnermoney['bal'] -= 50
            targetmoney['bal'] += 50
            botdb.set(cmdrunnermoneykey, cmdrunnermoney, "currency")
            botdb.set(targetmoneykey, targetmoney, "currency")
            lost="You lost **$50** when running away!"
          eremb=discord.Embed(title="Stealing [FAILED!]", description="Failed to steal from " + target.name + "! " + lost, color=0xFF0000)
          await self.bot.say(context.message.author.mention, embed=eremb)

##################
# Currency Admin #
##################

# Admin Balance - Add to, Take from, Set, or Reset a User balance (!abal ARG USER AMOUNT)
  @commands.command(pass_context=True)
  async def abal(self, context, arg : str = "add", target : discord.User = None, am : int = 150):
    if "494721265383374879" in [role.id for role in context.message.author.roles]:
      if target == None:
        erembed=discord.Embed(title="Error", description="Please specify a user, an argument, and an amount to add/take/set. (ex: !abal add @Steel_Dev#3344 150 - Set 0 to reset)", color=0xFF0000)
        await self.bot.say("", embed=erembed)
        return

      if arg == "add":
        if am < 0:
          erembed=discord.Embed(title="Error", description="Amount cannot be below $0.", color=0xFF0000)
          await self.bot.say("", embed=erembed)
          return   

        key = target.name + "_" + target.discriminator + "_money"
        money = botdb.get(key, "currency")
        money['bal'] += am
        botdb.set(key, money, "currency")
        adembed=discord.Embed(title="DragonScript Bank", description="User Balance Info", color=0x1abc9c)
        adembed.set_thumbnail(url=target.avatar_url)
        adembed.add_field(name=target.name + "'s Currency card", value="Card No/ID: **" + target.id + "**\nAdding **$" + am.__str__() + "** to " + target.name + "'s account.")
        await self.bot.say(target.mention, embed=adembed)
      elif arg == "rem" or arg == "take":
        if am <= 0:
          erembed=discord.Embed(title="Error", description="Amount cannot be below or equal to $0.", color=0xFF0000)
          await self.bot.say("", embed=erembed)
          return   

        key = target.name + "_" + target.discriminator + "_money"
        money = botdb.get(key, "currency")
        money['bal'] -= am
        botdb.set(key, money, "currency")
        seembed=discord.Embed(title="DragonScript Bank", description="User Balance Info", color=0x1abc9c)
        seembed.set_thumbnail(url=target.avatar_url)
        seembed.add_field(name=target.name + "'s Currency card", value="Card No/ID: **" + target.id + "**\nTaking **$" + am.__str__() + "** from " + target.name + "'s account.")
        await self.bot.say(target.mention, embed=seembed)
      elif arg == "set":
        if am < 0:
          erembed=discord.Embed(title="Error", description="Amount cannot be below $0.", color=0xFF0000)
          await self.bot.say("", embed=erembed)
          return
        
        if am == 0:
          moneykey = target.name + "_" + target.discriminator + "_money"
          botdb.set(moneykey, {'bal': 1000}, "currency")     
          resembed=discord.Embed(title="DragonScript Bank", description="User Balance Info", color=0x1abc9c)
          resembed.set_thumbnail(url=target.avatar_url)
          resembed.add_field(name=target.name + "'s Currency card", value="Card No/ID: **" + target.id + "**\nReset " + target.name + "'s Account Balance to the default **$1000**.")
          await self.bot.say(target.mention, embed=resembed)  
          return

        key = target.name + "_" + target.discriminator + "_money"
        money = botdb.get(key, "currency")
        money['bal'] = am
        botdb.set(key, money, "currency")
        seembed=discord.Embed(title="DragonScript Bank", description="User Balance Info", color=0x1abc9c)
        seembed.set_thumbnail(url=target.avatar_url)
        seembed.add_field(name=target.name + "'s Currency card", value="Card No/ID: **" + target.id + "**\nSet " + target.name + "'s Account Balance to **$" + am.__str__() + "**.")
        await self.bot.say(target.mention, embed=seembed)   
      else:
        erembed=discord.Embed(title="Error", description="Invalid Argument.", color=0xFF0000)
        await self.bot.say("", embed=erembed)
        return       
    else:
       erembed=discord.Embed(title="Error", description="You dont have permission to run this command.", color=0xFF0000)
       await self.bot.say("", embed=erembed)
       return

############
# Gambling #
############

# Slots - Slot machine command
  @commands.command(pass_context=True)
  @commands.cooldown(1, 30, commands.BucketType.user)
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
      ':hearts:',
      ':diamonds:',
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

# Roulette - Roullette machine command
  @commands.command(pass_context=True)
  @commands.cooldown(2, 20, commands.BucketType.user)
  async def roulette(self, context, bet : int = 0, num : int = -1, col : str = ""):
    key = context.message.author.name + "_" + context.message.author.discriminator + "_money"
    doc = botdb.get(key, "currency")

    if bet < 30 and num == -1 and col == "":
        erembed=discord.Embed(title="Error", description="Please place a bet, and what number you'd like to bet on, and what color. (ex: !roulette 20 5 green/black/red)", color=0xFF0000)
        await self.bot.say("", embed=erembed)
        return

    if bet < 30 or bet > 50:
        erembed=discord.Embed(title="Error", description="Bet must be between **$30-$50**", color=0xFF0000)
        await self.bot.say("", embed=erembed)
        return     

    if num < 0 or num > 10:
        erembed=discord.Embed(title="Error", description="Number you're betting on must be between **0-10**.", color=0xFF0000)
        await self.bot.say("", embed=erembed)
        return

    if col != "green" and col != "red" and col != "black":
        erembed=discord.Embed(title="Error", description="You can only bet on Green(number 0), Red(odd numbers), Black(even numbers)", color=0xFF0000)
        await self.bot.say("", embed=erembed)
        return

    if doc['bal'] >= bet:
      money = botdb.get(key, "currency")
      money['bal'] -= bet
      botdb.set(key, money, "currency")

      reward=0
      generatednum=randint(0,10)
      
      if col == "green" and generatednum == 0:
        reward=bet*2
      elif col == "red" and generatednum == 1:
        reward=bet*2
      elif col == "red" and generatednum == 3:
        reward=bet*2
      elif col == "red" and generatednum == 5:
        reward=bet*2  
      elif col == "red" and generatednum == 7:
        reward=bet*2
      elif col == "red" and generatednum == 9:
        reward=bet*2
      elif col == "black" and generatednum == 2:
        reward=bet*2
      elif col == "black" and generatednum == 4:
        reward=bet*2
      elif col == "black" and generatednum == 6:
        reward=bet*2
      elif col == "black" and generatednum == 8:
        reward=bet*2
      elif col == "black" and generatednum == 10:
        reward=bet*2
      else:
        reward=0

      if generatednum == num:
        reward=bet*10

      rouletteemb=discord.Embed(title="Roulette", description="Can you get lucky?\n**How it works:**\nIf the game generates a number that matches the one you bet on, your reward is 10 times your initial bet\nIf the generated number matches your color\nGreen/0 is 2x initial bet\nRed/Odd Numbers are 3x your initial bet\nBlack/Even Numbers are 4x your initial bet", color=0x1abc9c)
      rouletteemb.set_image(url="https://www.101computing.net/wp/wp-content/uploads/roulette.png")
      rouletteemb.add_field(name="Result", value="You bet **$"+bet.__str__()+"**, you bet on the number **"+num.__str__()+"** and you bet on the color **"+col.__str__()+"**\nThe generated number is: **"+generatednum.__str__()+"**")
      rouletteemb.add_field(name="Reward", value="You got.. **$"+reward.__str__()+"**!")
      money['bal'] += reward
      botdb.set(key, money, "currency")
      await self.bot.say(context.message.author.mention, embed=rouletteemb)
    else:
        erembed=discord.Embed(title="Error", description="You don't have enough to play this.", color=0xFF0000)
        await self.bot.say("", embed=erembed)
        return     

# Bot setup
def setup(bot):
  bot.add_cog(Chris(bot))
