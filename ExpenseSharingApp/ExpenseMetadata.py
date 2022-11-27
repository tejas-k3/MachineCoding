class ExpenseMetadata:
    def __init__(self, name: str, profilePic: str, notes: str):
        self.__name = name
        self.__profilePic = profilePic
        self.__notes = notes

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getprofilePic(self):
        return self.__profilePic

    def setprofilePic(self, profilePic: str):
        self.__profilePic = profilePic

    def getNotes(self):
        return self.__notes

    def setNotes(self, notes: str):
        self.__notes = notes
