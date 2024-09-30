weight_d40 = 900
mtom = 1280

weight_pilot = int(input("Gewicht Pilot: "))
weight_passenger = int(input("Gewicht Passagier: "))
weight_compartment = int(input("Standard compartment: "))
weight_fuel = int(input("Sprit: "))

weight_sum = weight_d40 + weight_pilot + weight_passenger + weight_compartment + weight_fuel

if weight_sum <= mtom:
    print("Allowed to take-off")
else:
    print("Not allowed to take-off")
