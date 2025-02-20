def calculate_celcius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Celsius [°C]: "))

print(f"{calculate_celcius_to_fahrenheit(celsius)} °F")

def calculate_weight(density, litres):
    return density * litres