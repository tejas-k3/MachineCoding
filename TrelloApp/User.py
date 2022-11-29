class User:
    def __init__(self, name):
        self.id = name
        self.userName = name
        self.userEmail = None

    # generic attributes update
    def updateName(self, newName):
        self.userName = newName

    def updateEmail(self, newEmail):
        self.userEmail = newEmail
