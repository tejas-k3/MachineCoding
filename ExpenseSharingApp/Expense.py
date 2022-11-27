from abc import ABC, abstractmethod
from ExpenseSharingApp.ExpenseMetadata import ExpenseMetadata
from ExpenseSharingApp.Split import Split
from ExpenseSharingApp.User import User


class Expense(ABC):
    def __init__(self, amount: float, paidBy: str, splits: list[Split], metadata: ExpenseMetadata):
        self.__amount = amount
        self.__paidBy = paidBy
        self.__splits = splits
        self.__metadata = metadata
        # self.__id = ''

    def getId(self):
        return self.__id

    def setId(self, id: str):
        self.__id = id

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount: float):
        self.__amount = amount

    def getPaidBy(self):
        return self.__paidBy

    def setPaidBy(self, paidBy: User):
        self.__paidBy = paidBy

    def getSplits(self):
        return self.__splits

    def setSplits(self, splits: list[Split]):
        self.__splits = splits

    def getMetadata(self):
        return self.__metadata

    def setMetadata(self, metadata: ExpenseMetadata):
        self.__metadata = metadata

    @abstractmethod
    def validate(self):
        pass
