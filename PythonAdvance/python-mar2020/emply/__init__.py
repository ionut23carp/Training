from bankaccs import BankAccount


class Employee:
    def __init__(self, name, account, salary=0):
        self.name = name
        self.bnkaccount = BankAccount(name, account)

    @property
    def salary(self):
        return None

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def receive_sal(self):
        self.bnkaccount.deposit(self.__salary)