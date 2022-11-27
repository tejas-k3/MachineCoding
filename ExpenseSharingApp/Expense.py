from abc import ABC, abstractmethod

import User
import Split


class Expense(ABC):
    def __init__(self, amount, paidBy, splits, metadata):
        self.amount = amount
        self.paidBy = paidBy
        self.splits = splits
        self.metadata = metadata

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount

    def getPaidBy(self):
        return self.__paidBy

    def setPaidBy(self, paidBy):
        self.__paidBy = paidBy

    def getSplits(self):
        return self.__splits

    def setSplits(self, splits):
        self.__splits = splits

    def getMetadata(self):
        return self.__metadata

    def setMetadata(self, metadata):
        self.__metadata = metadata

    @abstractmethod
    def validate(self):
        pass