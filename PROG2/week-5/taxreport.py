"""
Autohr: Gruppe 1
Date: 20.03.2025
Description: TODO
"""

from currency_converter import get_exchange_rate_to_chf

class TaxReport:
    """
    A class to generate a tax report for a bank application.
    """
    def generete(self, bank_application):
        """
        Generate tax report for the bank applications
		"""
        total_wealth = 0
        report = ["Tax Report:"]
        for account in bank_application:
            account_type = type(account).__name__.replace("Account", " Account")
            exchange_rate = get_exchange_rate_to_chf(account.currency)

            if exchange_rate is None:
                print(f"Wechselkurs konnte für {account.currency} nicht abrufen werden. Konto {account.identifier} wird übersprungen.")
                continue

            if account.currency == "CHF":
                report.append(f"** {account_type} ({account.identifier}) ** {account.balance:.2f} CHF")
                total_wealth += account.balance
            else:
                converted_balance = account.balance * exchange_rate
                report.append(f"** {account_type} ({account.identifier}) ** {account.balance:.2f} {account.currency} -> {converted_balance:.2f} CHF (Kurs: {exchange_rate:.4f})")
                total_wealth += converted_balance

        report.append("---------------------------")
        report.append(f"Total: {total_wealth:.2f} CHF")

        for line in report:
            print(line)
        
if __name__ == "__main__":
    from savingaccount import SavingAccount
    from youthaccount import YouthAccount

    accounts = [
        SavingAccount("S1", currency="USD", balance=1000),
        YouthAccount("Y1", owner_birthdate="2008-01-01", currency="EUR", balance=800),
        SavingAccount("S2", currency="CHF", balance=1200),
    ]

    tax_report = TaxReport()
    tax_report.generete(accounts)
        
