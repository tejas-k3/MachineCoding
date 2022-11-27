import User
import Split

class PercentSplit(Split):
    def __init__(self, user, percent):
        super(Split, self).__init__(user)
        self.__percent = percent
    def getPercent(self):
        return self.__percent
    def setPercent(self, percent):
        self.__percent = percent
