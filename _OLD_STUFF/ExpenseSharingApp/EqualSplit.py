from ExpenseSharingApp.User import User
from ExpenseSharingApp.Split import Split


class EqualSplit(Split):
    def __init__(self, user: User):
        super().__init__(user)
