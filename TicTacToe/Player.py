class Player:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.turnChar = ""
    def updateName(self,name):
        self.name = name
    def updateChar(self,char):
        self.turnChar = char
    def getChar(self):
        return self.turnChar