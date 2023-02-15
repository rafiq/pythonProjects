class Players:
    def __init__(self, user=True):
        self.name = user
        self.white = True

    def move(self):
        print(f"{self.player} moved")

    def setBlack(self, playerObj):
        playerObj.white = False
        print(f"player {playerObj.name} is black")