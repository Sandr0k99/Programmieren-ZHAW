import requests

_saved_exchange_rates = {}

def get_exchange_rate_to_chf(currency: str) -> float:
    """
    Gibt den Wechselkurs von einer Währung zu CHF zurück.
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

        if "rates" not in data or "CHF" not in data["rates"]:
            raise ValueError(f"Wechselkurs CHF für {currency} nicht gefunden.")

        rate = data["rates"]["CHF"]
        _saved_exchange_rates[currency] = rate
        return rate
    except Exception as e:
        raise RuntimeError(f"Fehler beim Abrufen des Wechselkurses {currency} -> CHF: {e}")


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Gibt den Wechselkurs von einer Währung zu einer anderen zurück, über CHF konvertiert. (double conversion)
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency == to_currency:
        return 1.0

    if from_currency == "CHF":
        # CHF -> Zielwährung
        rate_to_chf = get_exchange_rate_to_chf(to_currency)
        return 1 / rate_to_chf

    if to_currency == "CHF":
        # Startwährung -> CHF
        return get_exchange_rate_to_chf(from_currency)

    # Double conversion: Start -> CHF -> Ziel
    rate_from_to_chf = get_exchange_rate_to_chf(from_currency)
    rate_to_to_chf = get_exchange_rate_to_chf(to_currency)
    return rate_from_to_chf / rate_to_to_chf

if __name__ == "__main__":
    rate = get_exchange_rate("USD", "EUR")
    print(f"1 USD = {rate:.4f} EUR")
    rate = get_exchange_rate("CHF", "EUR")
    print(f"1 CHF = {rate:.4f} EUR")
    rate = get_exchange_rate("EUR", "CHF")
    print(f"1 EUR = {rate:.4f} CHF")
