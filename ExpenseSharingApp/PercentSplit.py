from ExpenseSharingApp.Split import Split
from ExpenseSharingApp.User import User


class PercentSplit(Split):
    def __init__(self, user:User, percent:float):
        super(Split, self).__init__(user)
        self.__percent = percent
    def getPercent(self):
        return self.__percent
    def setPercent(self, percent:float):
        self.__percent = percent
