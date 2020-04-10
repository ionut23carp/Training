class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(f'Please request amount below {self.balance}')
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


class SpecialBankAccount(BankAccount):
    def __init__(self, bank_name, balance, overdraft):
        super().__init__(bank_name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise InsufficientFundsException(f'Please request amount below {self.balance + self.overdraft}')
        self.balance -= amount
