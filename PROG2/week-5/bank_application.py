"""
Author: Gruppe 1
Date: 20.03.2025
Description: TODO
"""

#----------------------------------------------
# Imports
from bankaccount import BankAccount
from savingaccount import SavingAccount
from youthaccount import YouthAccount
from menu import Menu
from menu_entry import MenuEntry
from taxreport import TaxReport
#----------------------------------------------
# Class

VALID_CURRENCIES = {"CHF", "EUR", "USD", "GBP", "JPY", "CNY", "AUD", "CAD", "SEK", "NOK"} # Erlaubte Beispiel Währungen

class BankApplication():

    def __init__(self):
        self.accounts = []
        self.current_account = None
        self.menu = Menu("Bank Application")
        self.menu.add_entry(MenuEntry("Create new account", function=self.create_new_account, hotkey="1"))
        self.menu.add_entry(MenuEntry("Select Account", function=self.select_account, hotkey="2"))
        self.menu.add_entry(MenuEntry("Deposit money", function=self.deposit_money, hotkey="3"))
        self.menu.add_entry(MenuEntry("Withdraw money", function=self.withdraw_money, hotkey="4"))
        self.menu.add_entry(MenuEntry("Show balance", function=self.show_balance, hotkey="5"))
        self.menu.add_entry(MenuEntry("Close account", function=self.close_account, hotkey="6"))
        self.menu.add_entry(MenuEntry("Generate tax report", function=self.generate_tax_report, hotkey="7"))
        self.menu.add_entry(MenuEntry("Exit", function=self.exit, hotkey="8"))

    def create_new_account(self):
        """Create a new saving or youth account."""
        account_type = input("Enter account type (saving/youth): ").strip().lower()
        identifier = int(input("Enter account identifier: ").strip())

        while True:
            currency = input("Enter currency (e.g. CHF, EUR, USD): ").strip().upper()
            if not currency:
                currency = "CHF"
            if currency in VALID_CURRENCIES:
                break
            print(f"'{currency}' is no valid currency. Allowed are: {', '.join(VALID_CURRENCIES)}")

        if account_type == "saving":
            account = SavingAccount(identifier, currency=currency)
        elif account_type == "youth":
            birthday = input("Enter owner birthdate (YYYY-MM-DD): ")
            account = YouthAccount(identifier, owner_birthdate=birthday, currency=currency)
        else:
            print("Invalid account type.")
            return True
        self.accounts.append(account)
        print(f"{account_type} account created for {account.identifier}.")

    def select_account(self):
        """Select an account from the list of accounts."""
        if not self.accounts:
            print("No accounts available.")
            return True
        index = int(input("Select account number: "))
        for account in self.accounts:
             if account.identifier == index:
                self.current_account = account
                print(f"Selected account: {self.current_account.identifier}")
                return
             else:
                  print("Invalid account number.")

    def deposit_money(self):
        """Deposit money into the selected account."""
        if self.current_account is None:
            print("No account selected.")
            return True
        amount = float(input("Enter amount to deposit: "))
        self.current_account.deposit(amount)
        print(f"Deposited {amount} to {self.current_account.identifier}'s account.")

    def withdraw_money(self):
        """Withdraw money from the selected account."""
        if self.current_account is None:
            print("No account selected.")
            return
        amount = float(input("Enter amount to withdraw: "))
        self.current_account.withdraw(amount)
        print(f"Withdrew {amount} from {self.current_account.identifier}'s account.")

    def show_balance(self):
        """Show the balance of the selected account."""
        if self.current_account is None:
            print("No account selected.")
            return
        balance = self.current_account.get_balance()
        print(f"Balance for {self.current_account.identifier}'s account: {balance}")

    def close_account(self):
        """Close the selected account."""
        if self.current_account is None:
            print("No account selected.")
            return
        self.accounts.remove(self.current_account)
        print(f"Closed account of {self.current_account.identifier}.")
        self.current_account = None

    def exit(self):
        """Exit the application."""
        print("Exiting application.")
        exit()
        
    def generate_tax_report(self):
        """Generate a tax report for the selected account."""
        if self.current_account is None:
            print("No account selected.")
            return

        taxreport = TaxReport()
        taxreport.generete(self.accounts)

if __name__ == "__main__":
    app = BankApplication()
    while True:
    	app.menu.choose()