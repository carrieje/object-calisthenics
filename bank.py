from datetime import datetime

class Date:
    def __init__(self, day, month, year):
        self.date = datetime(year, month, day)

class Money:
    def __init__(self, amount):
        self.amount = amount

class Account:
    def __init__(self, opening_date):
        self.balance = Money(0.0)
        self.opening_date = opening_date

    def deposit(amount):
        self.content = ...

if __name__ == '__main__':

  today = Date(7, 1, 16)
  new_account = Account(today)

  fourty_two_bitcoin = Money(42.0)
  new_account.deposit(fourty_two_bitcoin)
