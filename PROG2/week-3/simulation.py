from bank_manager import SavingAccount, YouthAccount, BankAccount
from utils import sleep_and_simulate

def main():
    # Create accounts
    saving_account = SavingAccount(identifier="SA123", balance=1000)
    youth_account = YouthAccount(identifier="YA123", owner_birthdate="2005-03-14", balance=500)

    # Simulate deposits and withdrawals
    saving_account.deposit(200)
    saving_account.withdraw(50)
    saving_account.get_balance()

    youth_account.deposit(100)
    youth_account.withdraw(50)
    youth_account.get_balance()

    # Simulate passage of time
    print("Simulating 30 seconds (3 months)...")
    sleep_and_simulate(saving_account, 30)
    sleep_and_simulate(youth_account, 30)

    # Check balances after simulation
    saving_account.get_balance()
    youth_account.get_balance()

if __name__ == "__main__":
    main()
