mu = 0.3
g = 9.81

kmh: float = float(input("v0 [km/h]? "))
mps: float = kmh / 3.6

distance = 0.5 * mps ** 2 / (mu * g)
print(distance)
