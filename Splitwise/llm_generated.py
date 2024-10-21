from abc import ABC, abstractmethod
from typing import List, Dict


class User:
    def __init__(self, user_id: str, name: str, email: str, phone: str):
        """
        Represents a user in the Splitwise system.
        """
        self._user_id = user_id
        self._name = name
        self._email = email
        self._phone = phone

    # Getters and Setters using Pythonic @property
    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone


# Abstract class for Split, mimics Java's Split class
class Split(ABC):
    def __init__(self, user: User):
        self._user = user
        self._amount = 0

    @property
    def user(self):
        return self._user

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount


# Concrete split types
class EqualSplit(Split):
    def __init__(self, user: User):
        super().__init__(user)


class ExactSplit(Split):
    def __init__(self, user: User, amount: float):
        super().__init__(user)
        self._amount = amount


class PercentSplit(Split):
    def __init__(self, user: User, percent: float):
        super().__init__(user)
        self._percent = percent

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, percent: float):
        self._percent = percent


# Class for additional expense details (metadata)
class ExpenseMetadata:
    def __init__(self, name: str, img_url: str, notes: str):
        self._name = name
        self._img_url = img_url
        self._notes = notes

    @property
    def name(self):
        return self._name

    @property
    def img_url(self):
        return self._img_url

    @property
    def notes(self):
        return self._notes


# Abstract class Expense
class Expense(ABC):
    def __init__(self, amount: float, paid_by: User, splits: List[Split], metadata: ExpenseMetadata):
        self._id = None
        self._amount = amount
        self._paid_by = paid_by
        self._splits = splits
        self._metadata = metadata

    @property
    def amount(self):
        return self._amount

    @property
    def paid_by(self):
        return self._paid_by

    @property
    def splits(self):
        return self._splits

    @abstractmethod
    def validate(self) -> bool:
        pass


# Concrete expense types
class EqualExpense(Expense):
    def validate(self) -> bool:
        for split in self.splits:
            if not isinstance(split, EqualSplit):
                return False
        return True


class ExactExpense(Expense):
    def validate(self) -> bool:
        total_amount = self.amount
        sum_split_amount = sum(split.amount for split in self.splits if isinstance(split, ExactSplit))
        return total_amount == sum_split_amount


class PercentExpense(Expense):
    def validate(self) -> bool:
        total_percent = 100
        sum_split_percent = sum(split.percent for split in self.splits if isinstance(split, PercentSplit))
        return total_percent == sum_split_percent


# Enum-like class for expense types
class ExpenseType:
    EQUAL = 'EQUAL'
    EXACT = 'EXACT'
    PERCENT = 'PERCENT'


# Service to create expenses based on type
class ExpenseService:
    @staticmethod
    def create_expense(expense_type: str, amount: float, paid_by: User, splits: List[Split], metadata: ExpenseMetadata) -> Expense:
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, paid_by, splits, metadata)
        elif expense_type == ExpenseType.PERCENT:
            for split in splits:
                if isinstance(split, PercentSplit):
                    split.amount = (amount * split.percent) / 100.0
            return PercentExpense(amount, paid_by, splits, metadata)
        elif expense_type == ExpenseType.EQUAL:
            total_splits = len(splits)
            split_amount = round(amount / total_splits, 2)
            for split in splits:
                split.amount = split_amount
            # Correct rounding errors for the first split
            splits[0].amount += (amount - split_amount * total_splits)
            return EqualExpense(amount, paid_by, splits, metadata)


# Expense Manager to handle users, expenses, and balances
class ExpenseManager:
    def __init__(self):
        self.expenses: List[Expense] = []
        self.user_map: Dict[str, User] = {}
        self.balance_sheet: Dict[str, Dict[str, float]] = {}

    def add_user(self, user: User) -> None:
        self.user_map[user.user_id] = user
        self.balance_sheet[user.user_id] = {}

    def add_expense(self, expense_type: str, amount: float, paid_by_id: str, splits: List[Split], metadata: ExpenseMetadata) -> None:
        expense = ExpenseService.create_expense(expense_type, amount, self.user_map[paid_by_id], splits, metadata)
        self.expenses.append(expense)

        for split in expense.splits:
            paid_to_id = split.user.user_id
            if paid_to_id not in self.balance_sheet[paid_by_id]:
                self.balance_sheet[paid_by_id][paid_to_id] = 0.0
            if paid_by_id not in self.balance_sheet[paid_to_id]:
                self.balance_sheet[paid_to_id][paid_by_id] = 0.0

            self.balance_sheet[paid_by_id][paid_to_id] += split.amount
            self.balance_sheet[paid_to_id][paid_by_id] -= split.amount

    def show_balance(self, user_id: str) -> None:
        is_empty = True
        for paid_to_id, balance in self.balance_sheet[user_id].items():
            if balance != 0:
                is_empty = False
                self._print_balance(user_id, paid_to_id, balance)
        if is_empty:
            print("No balances")

    def show_balances(self) -> None:
        is_empty = True
        for user_id, balances in self.balance_sheet.items():
            for paid_to_id, balance in balances.items():
                if balance > 0:
                    is_empty = False
                    self._print_balance(user_id, paid_to_id, balance)
        if is_empty:
            print("No balances")

    def _print_balance(self, user1_id: str, user2_id: str, amount: float) -> None:
        user1_name = self.user_map[user1_id].name
        user2_name = self.user_map[user2_id].name
        if amount < 0:
            print(f"{user1_name} owes {user2_name}: {abs(amount)}")
        elif amount > 0:
            print(f"{user2_name} owes {user1_name}: {abs(amount)}")


# Example usage:
manager = ExpenseManager()
user1 = User("1", "Alice", "alice@example.com", "1234567890")
user2 = User("2", "Bob", "bob@example.com", "0987654321")

manager.add_user(user1)
manager.add_user(user2)

splits = [EqualSplit(user1), EqualSplit(user2)]
metadata = ExpenseMetadata("Lunch", "image_url", "Shared lunch expense")

manager.add_expense(ExpenseType.EQUAL, 100, "1", splits, metadata)

manager.show_balances()
