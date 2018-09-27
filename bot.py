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

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}!'.format(message)
        await bot.send_message(message.channel, msg)
    elif message.content.startswith('!Lucas'):
        msg = '***Sniffs intensely! <@322808830218207232>***'.format(message)
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
                    value="""**rawr** - A true dragons roar!  
                    **Lucas** Rememberance of our lost Dragon Legend.
                    **Gender** - Everything has a gender.
                    **obama** - Please don't.
                    **logan** - A questionable species indeed...
                    **8ball** - Ask the destiny 'bout your furtune!
                    **cade** - Know more of this sweet boye!
                    **kami** - What is he anyways?
                    **chris** - Know a lil' more about Chris, that great guy :3
                    **godhimself** - If you wish you see your new god""", inline=False)
    embed.add_field(name="Informational CMDs",
                   value="""**aboutds** - Learn a little 'bout DragonScript Arena!
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
async def lick(user):
    possible_responses = [
        'You taste good..',
        'Ew, you taste like a sweaty nerd..',
        'Oh god.. what the.. did you shower in some dudes sweat??',
        '*gags* oh god..',
        'Definitely swam in a septic tank..',
    ]
    await bot.say("*licks* " + user.mention + " .." + random.choice(possible_responses))
    
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
    await bot.say("Please try one of the following timezones:")
    await bot.say("\n".join(pytz.all_timezones))
    return
    
  locTz = pytz.timezone(place)
  locTime = datetime.now(locTz)
  await bot.say(locTime.strftime('%a %d %b %Y %H:%M:%S'))

@bot.command()
async def kami():
  await bot.say("He's not a god!")

@bot.command()
async def cade():
  await bot.say("Remembering my lost Friend :cry:")

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

@bot.command()
async def logan():
  await bot.say("Logan has entered the battle!")
    
@bot.command()
async def obama():
    embed=discord.Embed(title="Obunga Obama", description="Let the fear spread")
    embed.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/026/438/obamammaa.jpg")
    await bot.say("", embed=embed)
    
@bot.command()
async def gender():
    await bot.say("My gender? Code... :dragon_face:")

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = '*{0.title}* uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()

class Music:
    """Voice related commands.
    Works in multiple servers at once.
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        """Joins a voice channel."""
        try:
            print(channel)
            await self.create_voice_client(channel)
        except discord.ClientException:
            await self.bot.say('Ya estoy en el canal de voz...')
        except discord.InvalidArgument:
            await self.bot.say('Este no es un canal de voz...')
        else:
            await self.bot.say('Estoy listo para reproducir audio en ' + channel.name)

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        """Summons the bot to join your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        print(summoned_channel)
        if summoned_channel is None:
            await self.bot.say('No estás en un canal de voz')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        """Plays a song.
        If there is a song currently in the queue, then it is
        queued until the next song is done playing.
        This command automatically searches as well from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html
        """
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
            'format': 'bestaudio[ext=m4a]/best',
            'restrictfilenames': True,
            'noplaylist': True,
            'prefer_ffmpeg': True
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.35
            entry = VoiceEntry(ctx.message, player)
            await self.bot.say('Enqueued ' + str(entry))
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def vol(self, ctx, value : int):
        """Sets the volume of the currently playing song."""

        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            await self.bot.say('Set the volume to {:.0%}'.format(player.volume))

    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        """Pauses the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.pause()

    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Resumes the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def stop(self, ctx):
        """Stops playing audio and leaves the voice channel.
        This also clears the queue.
        """
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        """Vote to skip a song. The song requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('Not playing any music right now...')
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            await self.bot.say('Requester requested skipping song...')
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 1:
                await self.bot.say('Skip vote passed, skipping song...')
                state.skip()
            else:
                await self.bot.say('Skip vote added, currently at [{}/1]'.format(total_votes))
        else:
            await self.bot.say('You have already voted to skip this song.')

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        """Shows info about the currently played song."""

        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            await self.bot.say('Not playing anything.')
        else:
            skip_count = len(state.skip_votes)
            await self.bot.say('Now playing {} [skips: {}/3]'.format(state.current, skip_count))

def random_sentence():
    """Returns a formatted random line from a text file"""
    line = random.choice(open(config['frases'], encoding="utf8").readlines())
    parts = line.split('(')
    if len(parts) == 2:
        line = '"{}"\n—{}'.format(parts[0].strip(), parts[1][:-3])
        return line
    else:
        return line

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.
