class Card:
    def __init__(self, name):
        self.id = name
        self.name = name
        self.description = ""
        self.assignedUser = None

    # generic attributes update
    def updateName(self, newName):
        self.name = newName

    def updateDescription(self, newDescription):
        self.description = newDescription

    # already checked in userid in main system or not
    def addAssignedUser(self, userId):
        self.assignedUser = userId

    def removeAssignedUser(self):
        self.assignedUser = None
