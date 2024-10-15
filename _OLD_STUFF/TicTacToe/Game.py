from collections import deque
from TicTacToe.Player import Player
from TicTacToe.Board import Board

class Game:
    def __init__(self):
        self.Board = Board()
        self.players = deque()

    def getFreeCells(self):
        return self.Board.getFreeCells()

    def putChar(self, x:str, y:str, X0:str):
        self.Board.put(x, y, X0)

    def numberofPlayer(self):
        return len(self.players)

    def addPlayer(self, player:Player):
        if (self.numberofPlayer() == 2):
            return
        self.players.append(player)

    def assignChars(self):
        self.players[0].updateChar("X")
        self.players[1].updateChar("O")

    def startGame(self):
        if (self.numberofPlayer() != 2):
            return False
        self.assignChars()
        self.move()

    def nextChance(self):
        return self.players.popleft()

    def move(self):
        currPlayer = self.nextChance()
        options = self.getFreeCells()
        win = self.putChar("Any random x,y from options", currPlayer.getChar())
        if (win):
            return Player
        self.addPlayer(currPlayer)
