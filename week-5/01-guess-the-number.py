import random

random_number = random.randint(1,10)

while True:
    chosen_number = int(input("Welche Zahl habe ich gewählt? (1-10)"))

    if chosen_number == random_number:
        print("Hit")
        break
    elif chosen_number < random_number:
        print("Too low")
    else:
        print("Too high")