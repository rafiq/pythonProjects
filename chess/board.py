class Board:
    def __init__(self, width=8, height=8):
        self.board = [["_"] * width for _ in range(height)]

    def render(self):
        for r in self.board:
            print(r)

    def handleClick(self):
        print("click handled")

    def updateBoard(self, r, c, playerObj):
        self.board[r][c] = playerObj.name
        print(self.board)