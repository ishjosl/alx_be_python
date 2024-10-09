class BankAccount:
    def __init__(self, account_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += account
    def withdraw(self, amount):
        if amount > 0 and amount < self. _account_balance:
            self._account_balance -= account
        else:
            return False        
    def display_balance(self):
        print(f"Current balance: ${self._account_balance:2f}")


 