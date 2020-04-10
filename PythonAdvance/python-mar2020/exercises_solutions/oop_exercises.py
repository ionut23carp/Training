from bank_account import BankAccount, SpecialBankAccount
from employee import Employee


if __name__ == '__main__':
    ba = BankAccount('ING', 100)
    print(ba.bank_name)
    print(ba.balance)

    ba.deposit(100)
    ba.withdraw(150)
    print(ba.balance)

    try:
        ba.withdraw(100)
    except Exception as ex:
        print(ex)
    print(ba.balance)

    e = Employee('Alin', ba)
    print(e.name.upper())
    print(e.bank_account.balance)

    print(e.salary)
    e.salary = 800
    print(e.salary)

    e.receive_salary()
    print(e.bank_account.balance)

    sba = SpecialBankAccount('BCR', 100, 200)
    sba.withdraw(200)
    print(sba.balance)
    try:
        sba.withdraw(200)
    except Exception as ex:
        print(ex)
