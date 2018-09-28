# dragonbot
Discord bot for/by DragonScript Coding Club

Everyone that's a part of the DragonScript Coding Club can modify this bot- and add whatever they please!

# Quickstart for nooblets:
1. Try adding a new command. Edit bot.py. Look for the "rawr" command to use as a reference:

  ```python
@bot.command()
async def rawr():
    await bot.say("RAWR!!! :dragon_face:")
```

   This automatically creates a new command *!rawr*  

   E.g. if you add something like:

   ```python
@bot.command()
async def hello_world():
    await bot.say("hello_world")
```

   ... that will automatically create a new command *!hello_world*. Of course I'm sure you can be more creative than that.

2. Make your own Personality Module. Personality Modules contain code that you can load and unload from the bot using *!load* and *!unload*. 

   Personality Modules are stored in files that start with *ext_*. E.g. *ext_aaron.py*. To load this module you would call *!load aaron*. 

   To create your Personality Module, make a new file starting with *ext_*. E.g. *ext_chris.py*. In this case, you would call *!load chris* to activate it.

# For those who may forget:
The bot updates/rebuilds after a new change in the repo- building takes up to at least a minute. Be patient when testing new commands/features in the discord.

# Discord for those who arent in:
Hop on into the DragonScript Coding Club discord and say hi! https://discord.gg/5nuEXxK

# Logs
The logs can be accessed here: http://secretsciencelab.com/dragonbotlog.html
