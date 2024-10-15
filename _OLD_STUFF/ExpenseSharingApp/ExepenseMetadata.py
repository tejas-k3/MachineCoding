class ExpenseMetadata:
    def __init__(self, name, profilePic, notes):
        self.__name = name
        self.__profilePic = profilePic
        self.__notes = notes

    def getName(self):
        return self.name

    def setName(self, name):
        self.__name = name

    def getprofilePic(self):
        return self.__profilePic

    def setprofilePic(self, profilePic):
        self.__profilePic = profilePic

    def getNotes(self):
        return self.__notes

    def setNotes(self, notes):
        self.__notes = notes
