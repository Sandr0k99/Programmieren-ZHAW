import requests

_saved_exchange_rates = {}

def get_exchange_rate_to_chf(currency: str) -> float:
    """
    Get exchnage rate from currency to CHF

    Parameters:
    currency (str): currency code

    Returns:
    float: exchange rate to CHF
    """
    currency = currency.upper()
    if currency == "CHF":
        return 1.0

    # To reduce API call's return already saved rates
    if currency in _saved_exchange_rates:
        return _saved_exchange_rates[currency]

    url = f"https://open.er-api.com/v6/latest/{currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"].get("CHF")
        _saved_exchange_rates[currency] = (rate)
        return rate
    except Exception as e:
        print(f"Fehler beim Abrufen des Wechselkurses {currency}->CHF: {e}")
        return None

if __name__ == "__main__":
    test_currency = "USD"
    rate = get_exchange_rate_to_chf(test_currency)
    if rate:
        print(f"1 {test_currency} = {rate:.4f} CHF")
