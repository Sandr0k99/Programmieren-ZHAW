import random


def display_matches(matches):
    for _ in range(matches):
        print("=======O")
    print(f"|The stack has {matches} matches.|")


def player_turn(matches):
    while True:
        try:
            choice = int(input("How many matches do you want to draw? (1, 2, or 3): "))
            if choice in [1, 2, 3] and choice <= matches:
                return choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3 within the available matches.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_turn(matches):
    if matches % 4 == 0:
        choice = random.randint(1, min(3, matches))
    else:
        choice = matches % 4
    print(f"Computer draws {choice} match(es).")
    return choice


def main():
    matches = random.randint(10, 20)
    print("Welcome to the Draw a Match Game!")
    display_matches(matches)

    player_starts = random.choice([True, False])
    print("You start!" if player_starts else "Computer starts!")

    while matches > 0:
        if player_starts:
            matches -= player_turn(matches)
            display_matches(matches)
            if matches == 0:
                print("You lost! The computer wins!")
                break

            matches -= computer_turn(matches)
            display_matches(matches)
            if matches == 0:
                print("Computer lost! You win!")
                break
        else:
            matches -= computer_turn(matches)
            display_matches(matches)
            if matches == 0:
                print("Computer lost! You win!")
                break

            matches -= player_turn(matches)
            display_matches(matches)
            if matches == 0:
                print("You lost! The computer wins!")
                break


if __name__ == "__main__":
    main()
