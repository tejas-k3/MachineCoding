from ExpenseSharingApp.User import User
from ExpenseSharingApp.ExpenseType import ExpenseType
from ExpenseSharingApp.ExactExpense import ExactExpense
from ExpenseSharingApp.PercentSplit import PercentSplit
from ExpenseSharingApp.PercentExpense import PercentExpense
from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata
from ExpenseSharingApp.ExpenseService import ExpenseService

class ExpenseManager():
    def __init__(self):
        self.__expenses = []
        self.__userMap = {}
        self.__balanceSheet = {}

    def __printBalance(self, user1:str, user2:str, amount:float):
        user1Name = self.__userMap[user1]
        user2Name = self.__userMap[user2]
        if amount < 0:
            print(user1Name, " owes ", user2Name, ": ", abs(amount))
        elif amount > 0:
            print(user2Name, " owes ", user1Name, ": ", abs(amount))

    def addUser(self, user:User):
        self.__userMap[user.getId()]=user
        self.__balanceSheet[user.getId()]={}

    def addExpense(self, expenseType:ExpenseType, amount:float, paidBy:str, splits:list, expenseMetadata:ExpenseMetadata):
        expense = ExpenseService.createExpense(expenseType, amount, self.__userMap[paidBy], splits, expenseMetadata)
        self.__expenses.append(expense)
        for split in expense.getSplits():
            paidTo = split.getUser().getId()
            balances = self.__balanceSheet.get(paidBy)
            if paidTo not in balances:
                balances[paidTo] = 0.0
            balances[paidTo] = balances[paidTo] + split.getAmount()
            balances = self.__balanceSheet[paidTo]
            if paidBy not in balances:
                balances[paidBy]=0.0
            balances[paidBy] = balances[paidTo] - split.getAmount()

    def showBalance(self, userId:str):
        isEmpty=True
        for userBalance in self.__balanceSheet[userId]:
            if userBalance.getValue()!=0:
                isEmpty=False
                self.__printBalance(userId, userBalance.getKey(), userBalance.getValue())
        if isEmpty:
            print("No balance u poor")

    def showBalances(self):
        isEmpty = True
        for allBalances in self.__balanceSheet:
            for userBalance in allBalances.getValue():
                if userBalance.getValue() > 0:
                    isEmpty = False
                    self.__printBalance(allBalances.getKey(), userBalance.getKey(), userBalance.getValue())
        if isEmpty:
            print("No balance u poor")
