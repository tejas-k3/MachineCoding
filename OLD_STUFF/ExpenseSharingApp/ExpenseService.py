from ExpenseSharingApp.ExpenseType import ExpenseType
from ExpenseSharingApp.ExactExpense import ExactExpense
from ExpenseSharingApp.PercentSplit import PercentSplit
from ExpenseSharingApp.PercentExpense import PercentExpense
from ExpenseSharingApp.EqualExpense import EqualExpense
from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata

class ExpenseService():
    def createExpense(expenseType:ExpenseType, amount:float, paidBy:str, splits:list, expenseMetadata=None):
        match expenseType:
            case ExpenseType.EXACT:
                return ExactExpense(amount, paidBy, splits, expenseMetadata)
            case ExpenseType.PERCENT:
                for split in splits:
                    percentSplit = PercentSplit(split)
                    split.setAmount(amount * percentSplit.getPercent() / 100)
                return PercentExpense(amount, paidBy, splits, expenseMetadata)
            case ExpenseType.EQUAL:
                totalSplits = len(splits)
                splitAmount = round(amount*100/totalSplits)/100
                for split in splits:
                    split.setAmount(splitAmount)
                splits[0].setAmount(splitAmount + (amount - splitAmount*totalSplits))
                return EqualExpense(amount, paidBy, splits, expenseMetadata)
            case _:
                print("Oops nothing found! Clever code breaking")
                return None