from TrelloApp.Board import Board
from TrelloApp.User import User


class Trello:
    def __init__(self):
        self.boards = {}
        self.users = {}
        self.freeCards = {}  # unassigned cards to any board or list

    # Board attributes
    def addBoard(self, boardName):
        if (boardName in self.boards):
            print("Board with same name already exists")
        else:
            self.boards[boardName] = Board(boardName)

    def removeBoard(self, boardId):
        if (boardId not in self.boards):
            print("Board does not exist in system")
        else:
            del self.boards[boardId]

    ## User attributes
    def addUser(self, userName):
        if (userName in self.users):
            print("user with same name already exists")
        else:
            self.users[userName] = User(userName)

    def removeUser(self, userId):
        if (userId not in self.users):
            print("User does not exist in system")
        else:
            del self.users[userId]

    def validateUser(self, userId):
        if (userId in self.users):
            return True
        return False

    def validateBoard(self, boardId):
        if (boardId in self.boards):
            return True
        return False