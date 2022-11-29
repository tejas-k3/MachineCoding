class Board:
    def __init__(self, size=3):
        self.size = 3
        self.grid = [["" for i in range(3)] for j in range(3)]


    def getChar(self, x, y):
        return self.grid[x][y]

    def put(self, x, y, char):
        if (self.getChar(x, y) != ""):
                return "Invalid Move"
        self.grid[x][y] = char
        self.checkWinningPosition()


    def getFreeCells(self):
        cells = []
        for i in range(3):
            for j in range(3):
                if (self.grid[i][j] == ""):
                    cells.append((i, j))
        return cells


    def checkWinningPosition(self):
        pass
