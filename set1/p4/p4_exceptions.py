# Name: Cagampan, Rhamsus Joshua C.
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 23, 2026

def divide_numbers():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        result = first_number / second_number
    except ValueError:
        print("Invalid number. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Division attempt finished.")


def open_file():
    file_name = input("Enter the file name: ").strip()
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except (IsADirectoryError, PermissionError, UnicodeDecodeError, OSError) as error:
        print(f"Could not read the file: {error}")
    else:
        print("\nFile contents:")
        print(contents if contents else "(The file is empty.)")
    finally:
        print("File operation finished.")


def show_menu():
    print("\nSafe Menu Program")
    print("1. Divide two numbers")
    print("2. Open a file")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
