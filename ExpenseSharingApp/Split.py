from ExpenseSharingApp.User import User


class Split(User):
    def __init__(self, user:User):
        self.__user = user

    def getUser(self):
        return self.__user

    def setUser(self, user:User):
        self.__user = user

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount:float):
        self.__amount = amount
