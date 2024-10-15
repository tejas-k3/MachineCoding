from TicTacToe.Player import Player
from TicTacToe.Game import Game

player1 = Player(1, "Name1")
player2 = Player(2, "Name2")
Game = Game()
Game.addPlayer(player1)
Game.addPlayer(player2)

print(Game.startGame())
