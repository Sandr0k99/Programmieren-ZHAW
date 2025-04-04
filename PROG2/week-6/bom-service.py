import requests
import time

class BOMService:
    """
    Service zum Abrufen, Verarbeiten und Anzeigen von BOM-Daten.
    Holt die Daten von einem HTTP-Endpunkt im JSON-Format, filtert ungültige Einträge
    und gibt die Kosten tabellarisch aus.
    """

    def __init__(self, url, max_retries=5):
        self.url = url
        self.max_retries = max_retries
        self.bom_data = []

    def fetch_data(self):
        retries = 0
        backoff = 1

        while retries < self.max_retries:
            try:
                response = requests.get(self.url, timeout=5)
                if response.status_code == 200:
                    return response.json()
            except requests.RequestException:
                pass

            retries += 1
            time.sleep(backoff)
            backoff *= 2

        raise ConnectionError("Max retries exceeded. BOM service unavailable.")

    def repair_umlauts(self, text):
        replacements = {
            'Ã¤': 'ä',
            'Ã¶': 'ö',
            'Ã¼': 'ü',
            'Ã„': 'Ä',
            'Ã–': 'Ö',
            'Ãœ': 'Ü',
            '\u00fc': 'ü',
            '\u00f6': 'ö',
            '\u00e4': 'ä'
        }
        for wrong, right in replacements.items():
            text = text.replace(wrong, right)
        return text

    def parse_data(self, raw_data):
        for material, cost in raw_data.items():
            material = self.repair_umlauts(material)

            # Kosten müssen gültig sein
            if isinstance(cost, (int, float)) and cost > 0:
                self.bom_data.append((material, cost))

        self.bom_data.sort()

    def print_bom(self):
        total = 0
        print("MATERIAL        | COST")
        print("----------------+---------")
        for material, cost in self.bom_data:
            print(f"{material:<15} | {cost:>7.2f}") # Links 15 Zeichen breit; Rechts 7 zeichen breit und 2 Nachkommastellen
            total += cost
        print("----------------+---------")
        print(f"{'SUM':<15} | {total:>7.2f}")

    def run(self):
        raw_data = self.fetch_data()
        self.parse_data(raw_data)
        self.print_bom()


if __name__ == "__main__":
    service = BOMService("http://160.85.252.87")
    service.run()
