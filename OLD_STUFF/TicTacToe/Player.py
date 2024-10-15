class Player:
    def __init__(self,id:str,name:str):
        self.id = id
        self.name = name
        self.turnChar = ""
    def updateName(self,name:str):
        self.name = name
    def updateChar(self,char:str):
        self.turnChar = char
    def getChar(self):
        return self.turnChar