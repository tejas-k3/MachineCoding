from ExpenseSharingApp.User import User
from ExpenseSharingApp.Split import Split
from ExpenseSharingApp.ExpenseType import ExpenseType
from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata
from ExpenseSharingApp.ExpenseService import ExpenseService


class ExpenseManager():
    def __init__(self):
        self.expenses = []
        self.userMap = {}
        self.balanceSheet = {}

    def printBalance(self, user1: str, user2: str, amount: float):
        user1Name = self.userMap[user1].getName()
        user2Name = self.userMap[user2].getName()
        if amount < 0:
            print(user1Name, " owes ", user2Name, ": ", abs(amount))
        elif amount > 0:
            print(user2Name, " owes ", user1Name, ": ", abs(amount))

    def addUser(self, user: User):
        self.userMap[user.getId()] = user
        self.balanceSheet[user.getId()] = {}

    def addExpense(self, expenseType: ExpenseType, amount: float, paidBy: str, splits: list[Split],
                   expenseMetadata=None):
        expense = ExpenseService.createExpense(expenseType, amount, self.userMap[paidBy], splits, expenseMetadata)
        self.expenses.append(expense)
        for split in expense.getSplits():
            paidTo = split.getUser().getId()
            balances = self.balanceSheet.get(paidBy)
            if paidTo not in balances:
                balances[paidTo] = 0.0
            balances[paidTo] = balances[paidTo] + split.getAmount()
            balances = self.balanceSheet.get(paidTo)
            if paidBy not in balances:
                balances[paidBy] = 0.0
            balances[paidBy] = balances[paidBy] - split.getAmount()

    def showBalance(self, userId: str):
        isEmpty = True
        for user in self.balanceSheet[userId]:
            if self.balanceSheet[userId][user] != 0:
                isEmpty = False
                self.printBalance(userId, user, self.balanceSheet[userId][user])
        if isEmpty:
            print("No balance u poor")

    def showBalances(self):
        isEmpty = True
        for userId in self.balanceSheet:
            for user in self.balanceSheet[userId]:
                if self.balanceSheet[userId][user] > 0:
                    isEmpty = False
                    self.printBalance(userId, user,
                                        self.balanceSheet[userId][user])
        if isEmpty:
            print("No balance u all poor")
