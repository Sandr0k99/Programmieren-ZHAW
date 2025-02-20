import random


# Initialize the board with 'O' for ocean
def initialize_board():
    board = []
    for _ in range(10):
        row = ["O"] * 15
        board.append(row)
    return board


# Print the current board
def print_board(board):
    print("  A B C D E F G H I J K L M N O")
    row_num = 1
    for row in board:
        print(f"{row_num} {' '.join(row)}")
        row_num += 1


# Check if the guess is correct
def check_guess(ship_position, guess):
    return ship_position == guess


# Main game logic
def battleship_game():
    # Initialize board and ship position
    board = initialize_board()
    ship_row = random.randint(0, 9)  # Random row for the ship (0-indexed)
    ship_col = random.randint(0, 14)  # Random column for the ship (0-indexed)
    ship_position = (ship_row, ship_col)

    print("Welcome to Battleship! You have 10 guesses to find the ship.")

    guesses = 0
    while guesses < 10:
        print_board(board)

        # Get player's guess (column and row)
        guess_col = input("Guess the column (A-O): ").upper()
        guess_row = input("Guess the row (1-10): ")

        # Convert guess to board coordinates
        if guess_col not in "ABCDEFGHIJKLMNO" or not guess_row.isdigit() or not (1 <= int(guess_row) <= 10):
            print("Invalid input, please try again.")
            continue

        guess_col = ord(guess_col) - ord('A')
        guess_row = int(guess_row) - 1

        if (guess_row < 0 or guess_row >= 10 or guess_col < 0 or guess_col >= 15):
            print("Guess is out of bounds. Try again.")
            continue

        # Check if the guess is correct
        if check_guess(ship_position, (guess_row, guess_col)):
            print("Congratulations! You hit the ship!")
            board[guess_row][guess_col] = "X"
            break
        else:
            print("Missed!")
            board[guess_row][guess_col] = "X"  # Mark missed shot
            guesses += 1

        if guesses == 10:
            print("Game Over! You've used all your guesses.")
            print(f"The ship was at {chr(ship_col + 65)}{ship_row + 1}.")
            break


# Start the game
battleship_game()