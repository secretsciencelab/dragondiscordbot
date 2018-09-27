import discord
import os, random
from datetime import datetime
import pytz, us
from discord import Game
from discord.ext.commands import Bot

TOKEN = os.environ["DISCORD_TOKEN"]

BOT_PREFIX = ("$", "!")
bot = Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

def startDiscord():
  bot.run(TOKEN)

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
    embed.add_field(name="Available commands (CMD Prefix: '!' or '$')", value="For now we got:", inline=False) 
    embed.add_field(name="Random CMDs", 
                    value="""**hello** - Hello :D
                    **goodnight** - Happy Dragonscripting! :D
                    **lucas** - Sniffing ;)
                    **chris** - More about the amazing Chrissyboi :3
                    **kami** - What is he, really?
                    **cade** - Info about the nice gent :)
                    **logan** - The best soldier
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

@bot.command(name="time",
             pass_context=True)
async def dstime(ctx, place):
  if place not in pytz.all_timezones:
    # try US states
    place = us.states.lookup(place)
    if place:
      place = place.capital_tz
  
  if not place:
    await bot.say("Sorry, I don't know where that is")
    await bot.say("Please try one of the following timezones:")
    await bot.say("\n".join(pytz.all_timezones))
    return
    
  locTz = pytz.timezone(place)
  locTime = datetime.now(locTz)
  await bot.say(locTime.strftime('%a %d %b %Y %H:%M:%S'))

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
                   **Kami** - A pretty smart and cool dude- also trying their very best""", inline=False)
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
  await bot.say("***SNIFFING INTENSIFIES*** You smell guud " + context.message.author.mention + " ^-^")

@bot.command()
async def chris():
  await bot.say("Walls. He's the insane Dungeon Master, Though he can be a pretty nice dude most the time :D")

@bot.command()
async def kami():
  await bot.say("He's not a god!")

@bot.command()
async def cade():
  await bot.say("A really cool and nice dude :)")

@bot.command()
async def logan():
  await bot.say("Logan has entered the battle!")

@bot.command()
async def rawr():
    await bot.say("RAWR!!! :dragon_face:")

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
# Misc CMDs #
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
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    prefix = "ext_"
    bot.unload_extension(prefix + extension_name)
    await bot.say("{} unloaded.".format(extension_name))
