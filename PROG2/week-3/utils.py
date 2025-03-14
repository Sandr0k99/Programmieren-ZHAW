from datetime import datetime, timedelta

def simulate_months(account, months):
    """
    Simulate the passage of time and accrue interest for the given account.

    Parameters:
    account (BankAccount): The account to simulate.
    months (int): The number of months to simulate.
    """
    for _ in range(months):
        account.balance += account.balance * account.interest_rate
        print(f"Interest accrued. New balance: {account.balance} {account.currency}")

def sleep_and_simulate(account, seconds):
    """
    Sleep for the given number of seconds and simulate the passage of time.

    Parameters:
    account (BankAccount): The account to simulate.
    seconds (int): The number of seconds to sleep.
    """
    import time
    time.sleep(seconds)
    months = seconds // 10
    simulate_months(account, months)
