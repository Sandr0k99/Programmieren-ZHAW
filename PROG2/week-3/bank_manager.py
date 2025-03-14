# Imports
from datetime import datetime

# Classes
class BankAccount:
    """
       A class to represent a BackAccount.
    """
    def __init__(self, identifier, currency="Fr", balance=0):
        self.identifier = identifier
        self.currency = currency
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} {self.currency} eingezahlt. Neuer Kontostand: {self.balance} {self.currency}")
        else:
            print("Einzahlungsbetrag muss positiv sein.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} {self.currency} abgehoben. Neuer Kontostand: {self.balance} {self.currency}")
        else:
            print("Unzureichendes Guthaben oder ungültiger Betrag.")

    def get_balance(self):
        return f"Kontostand: {self.balance} {self.currency}"

if __name__ == "__main__":
    account = BankAccount("CH123456789")
    account.deposit(1000.50)
    account.withdraw(200.25)
    print(account.get_balance())
    
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


class SavingAccount(BankAccount):

	"""
	A class to represent a SavingAccount.
	"""
	def __init__(self, identifier, currency="Fr", balance=0, interest_rate=0.01, additional_charge = 0.02):
		"""
        Initialize a new SavingAccount instance.

        Parameters:
        identifier (str): The unique identifier for the account.
        currency (str): The currency of the account. Default is "Fr".
        balance (float): The initial balance of the account. Default is 0.
        interest_rate (float): The interest rate for the account. Default is 0.01.
        additional_charge (float): The additional charge for overdraft. Default is 0.02.
        """
		self.identifier = identifier
		self.currency = currency
		self.balance = balance
		self.interest_rate = interest_rate
		self.additional_charge = additional_charge

	def deposit(self, amount):
		"""
        Deposit money into the SavingAccount.

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
        Withdraw money from the SavingAccount.

        Parameters:
        amount (float): The amount of money to withdraw. Must be positive and less than or equal to the balance.
        """
		if amount > 0 and amount <= self.balance:
			self.balance -= amount
			print(f"{amount} {self.currency} abgehoben. Neuer Kontostand: {self.balance} {self.currency}")
		elif amount > self.balance:
			# adding additionale charge when withdrawing more than balance
			amount += self.additional_charge * amount
			self.balance -= amount
			print(f"{amount} {self.currency} abgehoben. Neuer Kontostand: {self.balance} {self.currency}")
			print(f"Zusätzliche Gebühr von {self.additional_charge * amount} {self.currency}")
		else:
			print("Unglitiger Betrag.")

	def get_balance(self):
		"""
		Get the balance of the SavingAccount.
		"""
		print(f"Kontostand: {self.balance} {self.currency}")
