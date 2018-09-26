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

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}!'.format(message)
        await bot.send_message(message.channel, msg)

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# makes "help" a fancier command~~
@bot.command(aliases=['help'])
async def h():
    embed=discord.Embed(title="About DragonBot", description="Im DragonBot, the one and only bot for DragonScript Arena Discord!", color=0x1abc9c)
    embed.add_field(name="Available commands (CMD Prefix: '!' or '$')", value="For now we got:", inline=False) 
    embed.add_field(name="Random CMDs", 
                    value="""**rawr** - A true dragons roar!\n
                    **8ball** - Ask the destiny 'bout your furtune!\n
                    **cade** - Know more of this sweet boye!\n
                    **kami** - What is he anyways?\n
                    **chris** - Know a lil' more about Chris, that great guy :3\n
                    **godhimself** - If you wish you see your new god""", inline=False)
    embed.add_field(name="Informational CMDs",
                   value="""**aboutds** - Learn a little 'bout DragonScript Arena!\n
                   **time** - Wanna know what time it is somewhere in the word?""", inline=False)   
    await bot.say("", embed=embed)

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
async def chris():
  await bot.say("Walls. He's the insane Dungeon Master, Though he can be a pretty nice dude most the time :D")

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
    return
    
  locTz = pytz.timezone(place)
  locTime = datetime.now(locTz)
  await bot.say(locTime.strftime('%a %d %b %Y %H:%M:%S'))

@bot.command()
async def kami():
  await bot.say("He's not a god!")

@bot.command()
async def cade():
  await bot.say("He's Helpful and Kind")

@bot.command()
async def aboutds():
  embed=discord.Embed(title="About Dragonscript Arena", description="Dragonscript arena is a game designed to help it's players learn JavaScript while controlling/programming an AI for their dragons to go into battle!", color=0x1abc9c)
  embed.set_thumbnail(url="https://i.imgur.com/6QgGoAq.png")
  embed.add_field(name="Developer", value="The wonderful game was developed by the one and only- Aaron! He's quite talented, and did really well on the game.", inline=False)
  embed.add_field(name="Play now", value="You can play the game free over at: https://dragonscriptarena.com", inline=False)
  await bot.say("", embed=embed)

@bot.command()
async def godhimself():
    embed=discord.Embed(title="God himself", description="***BOW DOWN TO YOUR NEW GOD!***")
    embed.set_image(url="https://cdn.discordapp.com/attachments/259844248772411393/494527371454447677/god_himself.jpg")
    await bot.say("", embed=embed)

def startDiscord():
  bot.run(TOKEN)
