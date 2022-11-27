import User


class Split(User):
    def __init__(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    def setUser(self, user):
        self.__user = user

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount
