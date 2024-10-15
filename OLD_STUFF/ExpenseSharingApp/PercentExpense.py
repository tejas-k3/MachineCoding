from ExpenseSharingApp.Expense import Expense
from ExpenseSharingApp.PercentSplit import PercentSplit as PSplit
from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata


class PercentExpense(Expense):
    def __init__(self, amount:float, paidBy:str, splits:list, expenseMetadata=None):
        super().__init__(amount, paidBy, splits, expenseMetadata)

    # @Overrides
    def validate(self):
        for split in super().getSplits():
            if not isinstance(split, PSplit):
                return False
        totalPercent = 100
        sumPercent = 0
        for split in super().getSplits():
            # Issue is below line
            exactSplit = PSplit(split)
            sumPercent += exactSplit.getPercent()

        if totalPercent != sumPercent:
            return False
        return True
