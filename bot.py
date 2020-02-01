import asyncio
import botdb
import discord
import logging
import os
import pytz
import random
import time
import us
from datetime import datetime
from discord import Game
from discord.ext.commands import Bot
from geopy.geocoders import Nominatim
from tzwhere import tzwhere

# References
# logging: https://discordpy.readthedocs.io/en/latest/logging.html

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

BOT_PREFIX = ("!")
bot = Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    #logging.info("DragonBot received:\n%s\n%s" \
    #    % (str(message.content), str(message.channel)))

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="Use !help"))

def startDiscord():
  # not calling bot.run() since there is no handling of bot disconnects
  # bot.run(DISCORD_TOKEN)

  loop = asyncio.get_event_loop()
  while True:
    try:
        loop.run_until_complete(bot.start(DISCORD_TOKEN))
    except Exception as e:
        logging.info("DragonBot error", e)
    logging.info("DragonBot restarting in 1 min...")
    time.sleep(60)

####################
# VV CMDs Below VV #
####################

# Please try to keep the code organized-
# Informational commands under the 'Informational CMDs' comment-
# and random things under the 'Random CMDs' comment ~ Chris

######################
# Informational CMDs #
######################
@bot.command(aliases=['help'])
async def h():
    embed=discord.Embed(title="About DragonBot", description="Im DragonBot, the one and only bot for DragonScript Arena Discord!", color=0x1abc9c)
    embed.add_field(name="Available commands (CMD Prefix: '!')", value="For now we got:", inline=False) 
    embed.add_field(name="Random CMDs", 
                    value="""**hello** - Hello :D
                    **goodnight** - Happy Dragonscripting! :D
                    **lucas** - Sniffing ;)
                    **chris** - More about the amazing Chrissyboi :3
                    **doomguy_chiquito** - What is he, really?
                    **Dragondrawer** - Learn about the dragon artist :D
                    **Cade** - Some basic information about me! :)
                    **logan** - The best soldier
                    **update 1** - da next update is here!
                    **sec** - ???
                    **ivanovic** - A strategist.
                    **rawr** - It's a dragon.. what do you expect?
                    **8ball** - Ask the virtual spirits from beyond.. anything..
                    **godhimself** - Bow to your new god!
                    **obama** - No longer our pres..
                    **gender** - The dragons sexual identity.""", inline=False)
    embed.add_field(name="Informational CMDs",
                   value="""**help** - this..
                   **aboutds** - Learn a little 'bout DragonScript Arena!
                   **time** - Wanna know what time it is somewhere in the word?
                   **botteam** - Learn some about the bots main team""", inline=False)   
    await bot.say("", embed=embed)

async def _geocodeTimezoneName(place):
    geolocator = Nominatim(user_agent="dragonbot")
    location = geolocator.geocode(place)
    w = tzwhere.tzwhere()
    return w.tzNameAt(location.latitude, location.longitude)
    
@bot.command(name="time",
             pass_context=True)
async def dstime(ctx, place):
  origPlace = place
  if place not in pytz.all_timezones:
    place = await _geocodeTimezoneName(place)
  
  if not place:
    await bot.say("Sorry, I don't know where %s is" % origPlace)
    await bot.say("Please try one of the following timezones: https://en.m.wikipedia.org/wiki/List_of_tz_database_time_zones")
    return
    
  locTz = pytz.timezone(place)
  locTime = datetime.now(locTz)
  await bot.say("The time in %s is %s" % (origPlace, locTime.strftime('%-I:%M %p, %a %d %b %Y')))

@bot.command()
async def aboutds():
  embed=discord.Embed(title="About Dragonscript Arena", description="Dragonscript arena is a game designed to help it's players learn JavaScript while controlling/programming an AI for their dragons to go into battle!", color=0x1abc9c)
  embed.set_thumbnail(url="https://i.imgur.com/6QgGoAq.png")
  embed.add_field(name="Developer", value="The wonderful game was developed by the one and only- Aaron! He's quite talented, and did really well on the game.", inline=False)
  embed.add_field(name="Play now", value="You can play the game free over at: https://dragonscriptarena.com", inline=False)
  await bot.say("", embed=embed)

# UPDATE THIS WHENEVER WE ADD A NEW MEMBER TO THE TEAM - AKA SOMEONE ELSE GETS INVITED TO THE REPO TO HELP OUT!
@bot.command()
async def botteam():
    embed=discord.Embed(title="DragonBot Team", description="The wonderful team of people working on this bot together", color=0x1abc9c)
    embed.add_field(name="Team", value="""**Aaron** - The leader.. don't mess with him! He'll sick his DragonAI on you!
                   **Chris** - A C# Programmer trying to do the do on python to help with this bot..
                   **Cade** - A wonderful dude also trying his best to help with the bot
                   **Logan** - Yet another wonderful human being helping out
                   **Ivanovic** - Just one more boy... but can speak Spanish
                   **Dragondrawer** - A person who trys but trying, wait what? 
                   **Doomguy_chiquito** - A pretty smart and cool dude- also trying their very best""", inline=False)
    await bot.say("", embed=embed)

###############
# Random CMDs #
###############
@bot.command(pass_context=True)
async def hello(context):
  await bot.say("Hello, " + context.message.author.mention + "!")

@bot.command(pass_context=True)
async def goodnight(context):
  await bot.say("Goodnight, " + context.message.author.mention + "! Happy DragonScripting!")

@bot.command(pass_context=True)
async def lucas(context):
  await bot.say("***SNIFFING INTENSIFIES***   You smell guud " + context.message.author.mention + " ^-^")

@bot.command()
async def chris():
  await bot.say("Walls. He's the insane Dungeon Master, Though he can be a pretty nice dude most the time :D")

@bot.command()
async def doomguy_chiquito():
  await bot.say("He's not a god!")

@bot.command()
async def Cade():
  await bot.say("Cade, An hardworking gent getting his future together. Future Auto Technician, I'm a great Counselor if you need some advice about life or anything!")

@bot.command()
async def logan():
  await bot.say("Logan has entered the battle!")

@bot.command()
async def ra():
  await bot.say("ra!:dragon_face:")

@bot.command()
async def sec():
    await bot.say("Secrets: nas!s, d!da")
    
@bot.command()
async def locomoto_mortis():
    await bot.say("You have locked @Secret Science Lab#2406's left leg")  
    
@bot.command()
async def ded():
    await bot.say("|x.x|")    
    
@bot.command()
async def dad():
    await bot.say("!dooom")
    
@bot.command()
async def dooom():
    await bot.say("doomguy chiquito the gallant. the end")
    
@bot.command()
async def Accio():
    await bot.say("summoned rice")
    
@bot.command()
async def Aguamenti():
    await bot.say("now your wand is a water canon!")
      
@bot.command()
async def spells():
    await bot.say("https://img.yumpu.com/58642360/1/500x640/harry-potter-spells.jpg")

@bot.command()
async def rawr():
    await bot.say("RAWR!!! :dragon_face:")
    
@bot.command()
async def Dragondrawer():
    await bot.say("He obviously draws dragons... :pencil2:")
    
@bot.command()
async def ivanovic():
    await bot.say("Ivan Gomez at your service, if you need talk or help with the Spanish just said.")
    
@bot.command(name='8ball',
             description="Answers a yes/no question.",
             brief="Answers from the beyond.",
             aliases=['eight_ball', 'eightball', '8-ball'],
             pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'this is 1/6',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    
@bot.command()
async def godhimself():
    embed=discord.Embed(title="God himself", description="***BOW DOWN TO YOUR NEW GOD!***")
    embed.set_image(url="https://cdn.discordapp.com/attachments/259844248772411393/494527371454447677/god_himself.jpg")
    await bot.say("", embed=embed)
    
@bot.command()
async def obama():
    embed=discord.Embed(title="Obunga Obama", description="Let the fear spread")
    embed.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/026/438/obamammaa.jpg")
    await bot.say("", embed=embed)
    
@bot.command()
async def gender():
    await bot.say("My gender? Code... :dragon_face:")


###############
#  Misc CMDs  #
###############
@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    prefix = "ext_"
    try:
        bot.load_extension(prefix + extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("Personality module **{}** loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    prefix = "ext_"
    bot.unload_extension(prefix + extension_name)
    await bot.say("Personality module **{}** unloaded.".format(extension_name))

@bot.command(pass_context=True)
async def setgame(context, gamename : str):
    if "494721265383374879" in [role.id for role in context.message.author.roles]:
       await bot.change_presence(game=discord.Game(name=gamename))
       embed=discord.Embed(title="Playing message updated", description="Playing message updated to '" + gamename + "'", color=0x1abc9c)
       await bot.say("", embed=embed)
    else:
       embed=discord.Embed(title="Error", description="You dont have permission to run this command.", color=0x1abc9c)
       await bot.say("", embed=embed)

@bot.command(pass_context=True)
async def setjoinmessage(context, msg : str = ""):
    if "494721265383374879" in [role.id for role in context.message.author.roles]:
        if msg == "":
            erremb=discord.Embed(title="Error", description="Message cannot be blank.", color=0xFF0000)
            await bot.say(context.message.author.mention, embed=erremb)  
            return
        else:
            botdb.set("dragonscriptserver_joinmessage", {'serverjoinmsg': msg}, "server")
            erremb=discord.Embed(title="New Member Join Message", description="Join Message updated to **'" + msg.__str__() + "'**\n([USER] will be replaced with the new members name, and [SERVER] will be replaced with the servers name)", color=0x32e00f)
            await bot.say(context.message.author.mention, embed=erremb) 
    else:
       embed=discord.Embed(title="Error", description="You dont have permission to run this command.", color=0x1abc9c)
       await bot.say("", embed=embed)

@bot.command(pass_context=True)
async def setleavemessage(context, msg : str = ""):
    if "494721265383374879" in [role.id for role in context.message.author.roles]:
        if msg == "":
            erremb=discord.Embed(title="Error", description="Message cannot be blank.", color=0xFF0000)
            await bot.say(context.message.author.mention, embed=erremb)  
            return
        else:
            botdb.set("dragonscriptserver_leavemessage", {'serverleavemsg': msg}, "server")
            erremb=discord.Embed(title="Member Leave Message", description="Leave Message updated to **'" + msg.__str__() + "'**\n([USER] will be replaced with the new members name, and [SERVER] will be replaced with the servers name)", color=0x32e00f)
            await bot.say(context.message.author.mention, embed=erremb) 
    else:
       embed=discord.Embed(title="Error", description="You dont have permission to run this command.", color=0x1abc9c)
       await bot.say("", embed=embed)        


############################
# Server Join/Leave Events #
############################
@bot.event
async def on_member_join(member):
    newmemberkey = member.name + "_" + member.discriminator + "_money"
    joinmessage = botdb.get("dragonscriptserver_joinmessage", "server")
    defaultjoinmsg="Welcome [USER] to [SERVER]! We hope you enjoy your time here :)"
    membername="**" + member.name + "**"
    if joinmessage == None:
        botdb.set("dragonscriptserver_joinmessage", {'serverjoinmsg': defaultjoinmsg}, "server")
        joinmessage = botdb.get("dragonscriptserver_joinmessage", "server")

    msg = joinmessage['serverjoinmsg'].__str__()
    if "[USER]" in msg:
        msg = msg.replace("[USER]", membername)

    if "[SERVER]" in msg:
        msg = msg.replace("[SERVER]", "**DragonScript Coding Club**")

    joinemb=discord.Embed(title="Welcome!", description=msg, color=0x32e00f)
    joinemb.set_thumbnail(url=member.avatar_url)
    await bot.send_message(discord.Object(id='476647778148286476'), member.mention, embed=joinemb)
    #await bot.channels.get("476647778148286476").send(member.mention, embed=joinemb)
    # Put new user into the currency DB to avoid errors with the currency system- with a user not being in the DB
    newusermoney = botdb.get(newmemberkey, "currency")

    if newusermoney == None:
       botdb.set(newmemberkey, {'bal': 1000}, "currency")

@bot.event
async def on_member_remove(member):
    leavemessage = botdb.get("dragonscriptserver_leavemessage", "server")
    defaultleavemsg="[USER] Just left [SERVER] :( Well, goodbye! We hope you at least had a good time here :)"
    membername="**" + member.name + "**"
    if leavemessage == None:
        botdb.set("dragonscriptserver_leavemessage", {'serverleavemsg': defaultleavemsg}, "server")
        leavemessage = botdb.get("dragonscriptserver_leavemessage", "server")

    msg = leavemessage['serverleavemsg'].__str__()
    if "[USER]" in msg:
        msg = msg.replace("[USER]", membername)

    if "[SERVER]" in msg:
        msg = msg.replace("[SERVER]", "**DragonScript Coding Club**")

    leaveemb=discord.Embed(title="Goodbye!", description=msg, color=0xFF0000)
    leaveemb.set_thumbnail(url=member.avatar_url)
    await bot.send_message(discord.Object(id='476647778148286476'), member.mention, embed=leaveemb)
    #await bot.channels.get("476647778148286476").send(member.mention, embed=joinemb)   


###################
# CMD Error Event #
###################
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, discord.ext.commands.CommandOnCooldown):
        erembed=discord.Embed(title="Error", description=':exclamation: This command is on cooldown, please try again in %.2fs' % error.retry_after, color=0xFF0000)
        await bot.send_message(ctx.message.channel, embed=erembed)
    elif isinstance(error, discord.ext.commands.CommandNotFound):
        erembed=discord.Embed(title="Error", description=':exclamation: Unknown command.', color=0xFF0000)
        await bot.send_message(ctx.message.channel, embed=erembed)
    raise error
