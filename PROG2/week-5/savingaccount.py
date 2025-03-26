from bankaccount import BankAccount

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
		return self.balance
