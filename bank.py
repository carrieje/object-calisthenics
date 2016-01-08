from datetime import datetime

class Date:
    def __init__(self, day, month, year):
        self.date = datetime(year, month, day)

class Money:
    def __init__(self, amount):
        self.amount = amount

class Account:
    def __init__(self, content, opening_date):
        self.content = content
        self.opening_date = opening_date

class AccountCollection:
    def __init__(self):
        self.content = list()

class Bank:
    def __init__ (self):
        self.account_list = list()

if __name__ == '__main__':
  print "hello bank"
