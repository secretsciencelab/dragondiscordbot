import discord
import random
from discord.ext import commands

rps = "rock", "paper", "scissor"

class Air():
    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def rock(self):
        
        if random.choice(rps) is "rock":
            await self.bot.say("I threw rock. The match is a draw.")
    
        elif random.choice(rps) is "scissor":
            await self.bot.say("I threw scissor. You win.")

        elif random.choice(rps) is "paper":
            await self.bot.say("I threw paper. I win")

    @commands.command()
    async def paper(self):
        if random.choice(rps) is "rock":
            await self.bot.say("I threw rock. You win.")
    
        elif random.choice(rps) is "scissor":
            await self.bot.say("I threw scissor. I win.")

        elif random.choice(rps) is "paper":
            await self.bot.say("I threw paper. The match is a draw.")

    @commands.command()
    async def scissors(self):
    
         if random.choice(rps) is "rock":
            await self.bot.say("I threw rock. I win.")
    
         if random.choice(rps) is "scissor":
            await self.bot.say("I threw scissor. The match is a draw.")

         if random.choice(rps) is "paper":
            await self.bot.say("I threw paper. You win.")

def setup(bot):
    bot.add_cog(Air(bot))
