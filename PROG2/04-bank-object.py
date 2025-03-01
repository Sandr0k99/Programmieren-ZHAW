class BankAccount:
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
    account.deposit(1000)
    account.withdraw(200)
    print(account.get_balance())