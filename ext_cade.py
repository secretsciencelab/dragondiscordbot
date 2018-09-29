import botdb
import discord
from discord.ext import commands

class Cade():
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def Help(self):
    await self.bot.say('I feel dead inside :D')

  @commands.command()
  async def dbset(self, key, value):
    botdb.set(key, {'value': value}, "cade")

  @commands.command()
  async def dbget(self, key):
    doc = botdb.get(key, "cade")
    if doc:
      await self.bot.say("%s" % doc['value'])
    else:
      await self.bot.say("Not found")
      
class Game:
    """ Checklist when adding a game:
        - Create class, extend Game, add all functions
        - Import game on top of the main file
        - In the main file, add it into the if/elif branch for !challenge
        - Add game onto !help game list
    """
    
    def __init__(self, players):
        self.players = players
        self.name = 'Generic game.'

  async def start(self, client, message):
        pass

  async def draw(self, client, message):
        pass
    
    def get_whose_turn(self):
        pass

  async def make_move(self, client, message):
        pass

    def is_over(self):
        pass

    def __repr__(self):
        return 'Generic repl'

class TicTacToe(Game):
    def __init__(self, players):
        Game.__init__(self, players)
        self.board = [' ']*9
        self.turn = players[0]
        self.over = False
        self.name = "tictactoe"

  async def start(self, client, message):
        await self.draw(client, message)

  async def draw(self, client, message):
        board = self.board

        t = ''
        t += str(self.players[0]) + ' vs ' + str(self.players[1])

        t += '\n```'
        t += '   |   |' + '\n'
        t += ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n'
        t += '   |   |' + '\n'
        t += '-----------' + '\n'
        t += '   |   |' + '\n'
        t += ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n'
        t += '   |   |' + '\n'
        t += '-----------' + '\n'
        t += '   |   |' + '\n'
        t += ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n'
        t += '   |   |' + '\n'
        t += '```\n'
        
        if not self.over:
            t += 'It is ' + str(self.turn) + '\'s turn.'

        await client.send_message(message.channel, t)
            

  async def make_move(self, client, message):
        i = int(message.content.split()[1])
        
        if i > 9 or i < 1 or self.board[i - 1] != ' ' :
            await client.send_message(message.channel, 'Error, can\'t place here')
            return
            
        if self.turn == self.players[0]:
            self.board[i - 1] = 'X'
            self.turn = self.players[1]
        else:
            self.board[i - 1] = 'O'
            self.turn = self.players[0]

        await self.draw(client, message)
        
        w = self.check_win()
        if w != False:
            self.over = True
            if w == 'X' or w == 'O': await client.send_message(message.channel, w + ' wins.')
            else: await client.send_message(message.channel, 'Tie.')

    def check_win(self):
        b = self.board
        if b[0] == b[1] and b[0] == b[2]:
            if b[0] == 'X': return 'X'
            elif b[0] == 'O': return 'O'
        if b[3] == b[4] and b[3] == b[5]:
            if b[3] == 'X': return 'X'
            elif b[3] == 'O': return 'O'
        if b[6] == b[7] and b[6] == b[8]:
            if b[6] == 'X': return 'X'
            elif b[6] == 'O': return 'O'
            
        if b[0] == b[3] and b[0] == b[6]:
            if b[0] == 'X': return 'X'
            elif b[0] == 'O': return 'O'
        if b[1] == b[4] and b[1] == b[7]:
            if b[1] == 'X': return 'X'
            elif b[1] == 'O': return 'O'
        if b[2] == b[5] and b[2] == b[8]:
            if b[2] == 'X': return 'X'
            elif b[2] == 'O': return 'O'

        if b[0] == b[4] and b[0] == b[8]:
            if b[4] == 'X': return 'X'
            elif b[4] == 'O': return 'O'
        if b[2] == b[4] and b[2] == b[6]:
            if b[4] == 'X': return 'X'
            elif b[4] == 'O': return 'O'

        if ' ' not in b: return 'T' # tie
        
        return False
    
    def get_whose_turn(self):
        return self.turn

    def is_over(self):
        return self.over

    def __repr__(self):
        return str(self.players[0]) + ' vs ' + str(self.players[1]) + ' playing ' + self.name + '\n'


class XTacToe(Game):
    def __init__(self, players):
        Game.__init__(self, players)
        self.board = [' ']*9
        self.turn = players[0]
        self.over = False
        self.name = "xtactoe"

  async def start(self, client, message):
        await self.draw(client, message)

  async def draw(self, client, message):
        board = self.board

        t = ''
        t += str(self.players[0]) + ' vs ' + str(self.players[1])

        t += '\n```'
        t += '   |   |' + '\n'
        t += ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n'
        t += '   |   |' + '\n'
        t += '-----------' + '\n'
        t += '   |   |' + '\n'
        t += ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n'
        t += '   |   |' + '\n'
        t += '-----------' + '\n'
        t += '   |   |' + '\n'
        t += ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n'
        t += '   |   |' + '\n'
        t += '```\n'
        
        if not self.over:
            t += 'It is ' + str(self.turn) + '\'s turn.'

        await client.send_message(message.channel, t)
            

  async def make_move(self, client, message):
        i = int(message.content.split()[1])
        
        if i > 9 or i < 1 or self.board[i - 1] != ' ' :
            await client.send_message(message.channel, 'Error, can\'t place here')
            return
            
        self.board[i - 1] = 'X'
        if self.turn == self.players[0]:
            self.turn = self.players[1]
        else:
            self.turn = self.players[0]

        await self.draw(client, message)
        
        w = self.check_win()
        if w != False:
            self.over = True
            await client.send_message(message.channel, str(self.turn) + ' wins.')

    def check_win(self):
        b = self.board
        if b[0] == b[1] and b[0] == b[2]:
            if b[0] == 'X': return 'X'
        if b[3] == b[4] and b[3] == b[5]:
            if b[3] == 'X': return 'X'
        if b[6] == b[7] and b[6] == b[8]:
            if b[6] == 'X': return 'X'
            
        if b[0] == b[3] and b[0] == b[6]:
            if b[0] == 'X': return 'X'
        if b[1] == b[4] and b[1] == b[7]:
            if b[1] == 'X': return 'X'
        if b[2] == b[5] and b[2] == b[8]:
            if b[2] == 'X': return 'X'

        if b[0] == b[4] and b[0] == b[8]:
            if b[4] == 'X': return 'X'
        if b[2] == b[4] and b[2] == b[6]:
            if b[4] == 'X': return 'X'
        
        return False
    
    def get_whose_turn(self):
        return self.turn

    def is_over(self):
        return self.over

    def __repr__(self):
        return str(self.players[0]) + ' vs ' + str(self.players[1]) + ' playing ' + self.name + 
      
def setup(bot):
  bot.add_cog(Cade(bot))
