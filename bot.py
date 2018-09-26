import discord
import os, random
from discord import Game
from discord.ext.commands import Bot

TOKEN = os.environ["DISCORD_TOKEN"]

BOT_PREFIX = ("?", "!")
bot = Bot(command_prefix=BOT_PREFIX)

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

@bot.command()
async def help():
    embed=discord.Embed(title="About DragonBot", description="Im DragonBot, the one and only bot for DragonScript Arena Discord!", color=0x1abc9c)
    embed.add_field(name="Available commands", value="For now we got:", inline=False)
    embed.add_field(name="rawr", value="A true dragon's roar!", inline=False)
    embed.add_field(name="8ball", value="Ask the destiny 'bout your fortune!", inline=False)
    embed.add_field(name="chris", value="Know a lil' bit more 'bout Chirs, that great guy. :3", inline=False)
    embed.add_field(name="kami", value="What is he anyways?", inline=False)
    embed.add_field(name="aboutds", value="To tell you 'bout DragonScript Arena!", inline=False)

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
  await bot.say("Walls.")

@bot.command()
async def kami():
  await bot.say("He's not a god!")

@bot.command()
async def aboutds():
  embed=discord.Embed(title="About Dragonscript Arena", description="Dragonscript arena is a game designed to help it's players learn JavaScript while controlling/programming an AI for their dragons to go into battle!", color=0x1abc9c)
  embed.set_thumbnail(url="https://i.imgur.com/6QgGoAq.png")
  embed.add_field(name="Developer", value="The wonderful game was developed by the one and only- Aaron! He's quite talented, and did really well on the game.", inline=False)
  embed.add_field(name="Play now", value="You can play the game free over at: https://dragonscriptarena.com", inline=False)
  await bot.say("", embed=embed)

def startDiscord():
  bot.run(TOKEN)
