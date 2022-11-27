from ExpenseSharingApp.User import User
from ExpenseSharingApp.Split import Split


class ExactSplit(Split):
    def __init__(self, user:User, amount:float):
        super(Split, self).__init__(user)
        self.__amount = amount
