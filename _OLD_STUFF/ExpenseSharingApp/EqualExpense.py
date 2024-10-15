from ExpenseSharingApp.Expense import Expense
from ExpenseSharingApp.EqualSplit import EqualSplit
from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata
from ExpenseSharingApp.User import User
from ExpenseSharingApp.Split import Split


class EqualExpense(Expense):
    def __init__(self, amount: float, paidBy: User, splits: list[Split], expenseMetadata=None):
        super().__init__(amount, paidBy, splits, expenseMetadata)

    # @Overrides
    def validate(self):
        for split in super().getSplits():
            if not isinstance(split, EqualSplit):
                return False
        return True
