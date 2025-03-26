from bankaccount import BankAccount
from datetime import datetime

class YouthAccount(BankAccount):
    """
    A class to represent a YouthAccount.
    """
    def __init__(self, identifier, owner_birthdate, currency="Fr", balance=0, interest_rate=0.02, withdraw_limit=2000):
        """
        Initialize a new YouthAccount instance.

        Parameters:
        identifier (str): The unique identifier for the account.
        owner_birthdate (str): The birthdate of the account owner in the format 'YYYY-MM-DD'.
        currency (str): The currency of the account. Default is "Fr".
        balance (float): The initial balance of the account. Default is 0.
        interest_rate (float): The interest rate for the account. Default is 0.02.
        withdraw_limit (float): The monthly withdraw limit. Default is 2000.
        """
        birthdate = datetime.strptime(owner_birthdate, '%Y-%m-%d')
        age = (datetime.now() - birthdate).days // 365
        if age > 25:
            raise ValueError("Account owner must be 25 years old or younger.")
        
        super().__init__(identifier, currency, balance)
        self.interest_rate = interest_rate
        self.withdraw_limit = withdraw_limit
        self.withdrawn_this_month = 0

    def deposit(self, amount):
        """
        Deposit money into the YouthAccount.

        Parameters:
        amount (float): The amount of money to deposit. Must be positive.
        """
        if amount > 0:
            self.balance += amount
            print(f"{amount} {self.currency} eingezahlt. Neuer Kontostand: {self.balance} {self.currency}")
        else:
            print("Einzahlungsbetrag muss positiv sein.")

    def withdraw(self, amount):
        """
        Withdraw money from the YouthAccount.

        Parameters:
        amount (float): The amount of money to withdraw. Must be positive and within the monthly limit.
        """
        if amount > 0 and amount <= self.balance:
            if self.withdrawn_this_month + amount > self.withdraw_limit:
                print(f"Cannot withdraw {amount} {self.currency}. Monthly limit of {self.withdraw_limit} {self.currency} exceeded.")
            else:
                self.balance -= amount
                self.withdrawn_this_month += amount
                print(f"{amount} {self.currency} abgehoben. Neuer Kontostand: {self.balance} {self.currency}")
        else:
            print("Unglitiger Betrag.")

    def get_balance(self):
        """
        Get the balance of the YouthAccount.
        """
        print(f"Kontostand: {self.balance} {self.currency}")

    def reset_withdraw_limit(self):
        """
        Reset the monthly withdraw limit.
        """
        self.withdrawn_this_month = 0