import players
import board
import pygame
   
class Game:
    def __init__ (self, player1, player2=None):
        self.board = board.Board(8,8)
        self.player1 = player1
        self.player2 = player2
        if not player2:
            self.player2 = players.Players("computer")
        self.player2.setBlack(self.player2)

    def main(self):#add players here
        turn = True
        move = None
        x, y = "", ""
        while True:
            self.board.render()
            print(f"Make a move {player1 if turn else player2}")
            if turn:
                player1.move()
                x, y = input("? ")

                if x == "b":
                    return False
                self.board.updateBoard(int(x), int(y))
            else:
                player2.move()
                # player2.move()
                x, y = input("? ")
                if x == "b":
                    return False
                #check game status
                self.board.updateBoard(int(x), int(y))
            turn = not turn

player1 = players.Players("player1")
player2 = players.Players("player2")
game = Game(player1)
game.main()