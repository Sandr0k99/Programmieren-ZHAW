dominos = []

for num1 in range(7):
    for num2 in range(num1, 7):
        dominos.append([num1, num2])

for domino in dominos:
    print(f"{domino[0]}|{domino[1]}")