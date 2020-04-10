
class BankAccount:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def withdraw(self, value):
        assert value < self.money
        self.money -= value
        raise ValueError

    def deposit(self, value):
        self.money += value


class SpecialBankAccount(BankAccount):
    def __init__(self, name, money, overdraft):
        super().__init__(name, money)
        self.overdraft = overdraft

    def withdraw(self, value):
        assert value < self.money + self.overdraft
        self.money -= value
        raise Exception("Value exceeds {}".format(self.money + self.overdraft))