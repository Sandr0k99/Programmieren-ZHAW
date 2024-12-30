def print_numbers(numbers):
    if not numbers:
        print("The phone book is empty.")
    else:
        for name, number in numbers.items():
            print(f"{name}: {number}")


def add_number(numbers, name, number):
    if name in numbers:
        print(f"{name} is already in the phone book. Updating their number.")
    numbers[name] = number
    print(f"Added/Updated {name}'s number to {number}.")


def lookup_number(numbers, name):
    return numbers.get(name, "Contact not found.")


def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
        print(f"Removed {name} from the phone book.")
    else:
        print(f"{name} was not found in the phone book.")


def load_numbers(numbers, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, number = line.strip().split(':')
                numbers[name] = number
        print(f"Loaded contacts from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def save_numbers(numbers, filename):
    try:
        with open(filename, 'w') as file:
            for name, number in numbers.items():
                file.write(f"{name}:{number}\n")
        print(f"Saved contacts to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()


phone_book = {}
menu_choice = 0
print_menu()
while True:
    try:
        menu_choice = int(input("Type in a number (1-7): "))
        if menu_choice == 1:
            print_numbers(phone_book)
        elif menu_choice == 2:
            print("Add Name and Number")
            name = input("Name: ")
            phone = input("Number: ")
            add_number(phone_book, name, phone)
        elif menu_choice == 3:
            print("Remove Name and Number")
            name = input("Name: ")
            remove_number(phone_book, name)
        elif menu_choice == 4:
            print("Lookup Number")
            name = input("Name: ")
            print(lookup_number(phone_book, name))
        elif menu_choice == 5:
            filename = input("Filename to load: ")
            load_numbers(phone_book, filename)
        elif menu_choice == 6:
            filename = input("Filename to save: ")
            save_numbers(phone_book, filename)
        elif menu_choice == 7:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
    except ValueError:
        print("Please enter a valid number.")
