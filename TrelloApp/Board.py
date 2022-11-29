class Board:
    def __init__(self, name):
        self.id = name
        self.name = name
        self.privacy = "PUBLIC"
        self.url = "http://fakeTrello/" + str(self.id)
        self.members = {}
        self.lists = {}

    # generic attributes update
    def updateName(self, newName):
        self.name = newName

    def updatePrivacy(self, newPrivacy):
        self.privacy = newPrivacy

    # already checked in userid in main system or not
    def addMember(self, userId):
        if (userId in self.members):
            print("user already exists in Board")
        else:
            self.members[userId] = 1

    # already checked in userid in main system or not
    def removeMember(self, userId):
        if (userId not in self.members):
            print("user does not exist in Board")
        else:
            del self.members[userId]

    # any prev check needed yet to decide
    def addList(self, listId):
        if (listId in self.lists):
            print("list already exists in Board")
        else:
            self.lists[listId] = 1

    # any prev check needed yet to decide
    def removeList(self, listId):
        if (listId not in self.lists):
            print("list does not exist in Board")
        else:
            del self.lists[listId]