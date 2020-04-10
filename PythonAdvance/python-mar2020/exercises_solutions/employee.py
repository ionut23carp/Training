class Employee:
    def __init__(self, name, bank_account, salary=0):
        self.name = name
        self.bank_account = bank_account
        self.__salary = salary

    @property
    def salary(self):
        return None

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def receive_salary(self):
        self.bank_account.deposit(self.__salary)
