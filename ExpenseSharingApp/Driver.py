from ExpenseSharingApp.ExpenseManager import ExpenseManager
from ExpenseSharingApp.User import User
from ExpenseSharingApp.EqualSplit import EqualSplit
from ExpenseSharingApp.ExactSplit import ExactSplit
from ExpenseSharingApp.PercentSplit import PercentSplit
from ExpenseSharingApp.ExpenseType import ExpenseType
# from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata

def main():
    expenseManager = ExpenseManager()
    expenseManager.addUser(User("u1", "User1", "a@gmail.com", "9999999999"))
    expenseManager.addUser(User("u2", "User2", "b@gmail.com", "9999999998"))
    expenseManager.addUser(User("u3", "User3", "c@gmail.com", "9999999997"))
    expenseManager.addUser(User("u4", "User4", "d@gmail.com", "9999999996"))
    while True:
        command = input()
        commands = command.split()
        commandType = commands[0]
        match commandType:
            case "SHOW":
                if len(commands) == 1:
                    expenseManager.showBalances()
                else:
                    expenseManager.showBalance(commands[1])
            case "EXPENSE":
                paidBy = commands[1]
                amount = float(commands[2])
                countUsers = int(commands[3])
                expenseType = commands[4 + countUsers]
                splits = []
                match expenseType:
                    case "EQUAL":
                        for i in range(countUsers):
                            splits.append(EqualSplit(expenseManager.userMap[commands[4 + i]]))
                        expenseManager.addExpense(ExpenseType.EQUAL, amount, paidBy, splits, None)

                    case "EXACT":
                        for i in range(countUsers):
                            splits.append(
                                ExactSplit(expenseManager.userMap[commands[4 + i]], commands[5 + countUsers + i]))
                        expenseManager.addExpense(ExpenseType.EXACT, amount, paidBy, splits, None)
                    case "PERCENT":
                        for i in range(countUsers):
                            splits.append(
                                PercentSplit(expenseManager.userMap[commands[4 + i]], commands[5 + countUsers + i]))
                        expenseManager.addExpense(ExpenseType.PERCENT, amount, paidBy, splits, None)


if __name__ == "__main__":
    main()
else:
    print("Executed when imported")
