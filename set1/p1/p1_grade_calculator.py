def accept_grades():
    """Ask the user for a set of grades and return them as numbers."""
    while True:
        try:
            count = int(input("How many grades would you like to enter? "))
            if count > 0:
                break
            print("Enter a number greater than zero.")
        except ValueError:
            print("Enter a whole number.")

    grades = []
    for index in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {index + 1} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("A grade must be from 0 to 100.")
            except ValueError:
                print("Enter a valid number.")
    return grades


def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)


def get_pass_fail_status(grades):
    return "Passed" if compute_average(grades) >= 75 else "Failed"


def show_results(grades):
    if not grades:
        print("No grades are available. Choose option 1 first.")
        return

    print(f"\nAverage: {compute_average(grades):.2f}")
    print(f"Highest: {get_highest_grade(grades):.2f}")
    print(f"Lowest: {get_lowest_grade(grades):.2f}")
    print(f"Status: {get_pass_fail_status(grades)}")


def show_menu():
    print("\nStudent Grade Calculator")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")


def main():
    grades = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            grades = accept_grades()
            print(f"{len(grades)} grade(s) saved.")
        elif choice == "2":
            show_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()


# The grades list inside main is local to that function, so other functions cannot access it by name.
# A global variable is defined outside functions and can be accessed throughout the module.
# This program passes grades into the functions that need them instead of relying on a global grades list.
# That makes each calculation easier to understand and reuse with different grade lists.
