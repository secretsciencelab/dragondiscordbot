import discord
import random
from discord.ext import commands

rps = "rock", "paper", "scissor"

class Air():
    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def rockpaperscissor(self, str):
    
        if str is "rock" or "Rock" or "ROCK":

            if random.choice(rps) is "rock":
                await self.bot.say("I threw rock. The match is a draw.")
    
            elif random.choice(rps) is "scissor":
                await self.bot.say("I threw scissor. You win.")

            elif random.choice(rps) is "paper":
                await self.bot.say("I threw paper. I win")

        elif str is "paper" or "Paper" or "PAPER":

            if random.choice(rps) is "rock":
                await self.bot.say("I threw rock. You win.")
    
            elif random.choice(rps) is "scissor":
                await self.bot.say("I threw scissor. I win.")

            elif random.choice(rps) is "paper":
                await self.bot.say("I threw paper. The match is a draw.")

        elif str is "scissor" or "Scissor" or "SCISSOR":
    
            if random.choice(rps) is "rock":
                await self.bot.say("I threw rock. I win.")
    
            if random.choice(rps) is "scissor":
                await self.bot.say("I threw scissor. The match is a draw.")

            if random.choice(rps) is "paper":
                await self.bot.say("I threw paper. You win.")

        else:
            await self.bot.say("Please write rock paper or scissor")


def setup(bot):
    bot.add_cog(Air(bot))
