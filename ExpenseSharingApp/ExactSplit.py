import User
import Split


class ExactSplit(Split):
    def __init__(self, user, amount):
        super(Split, self).__init__(user)
        self.__amount = amount
