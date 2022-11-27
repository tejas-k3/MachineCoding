from ExpenseSharingApp.Expense import Expense
from ExpenseSharingApp.ExactSplit import ExactSplit
from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata
from ExpenseSharingApp.User import User
from ExpenseSharingApp.Split import Split

class ExactExpense(Expense):
    def __init__(self, amount: float, paidBy: User, splits: list[Split], expenseMetadata: ExpenseMetadata):
        super().__init__(amount, paidBy, splits, expenseMetadata)

    # @Overrides
    def validate(self):
        for split in super().getSplits():
            if not isinstance(split, ExactSplit):
                return False
        totalAmount = super().getAmount()
        sumSplit = 0
        for split in super().getSplits():
            # Issue is below line
            exactSplit = ExactSplit(split)
            sumSplit += exactSplit.getAmount()

        if totalAmount != sumSplit:
            return False
        return True
