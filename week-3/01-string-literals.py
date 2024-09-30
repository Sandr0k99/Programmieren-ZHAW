character = input('char: ')
reps = int(input('reps: '))

max_len = (reps + 1) // 2

for i in range(1, reps + 1):
    if i <= max_len:
        print(character * i)  # Aufsteigender Teil
    else:
        print(character * (reps - i + 1))  # Absteigender Teil
