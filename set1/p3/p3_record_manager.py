def add_student(students, student_keys):
    name = input("Enter the student's name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    key = name.casefold()
    if key in student_keys:
        print(f"{name} is already in the records.")
        return

    students.append(name)
    student_keys.add(key)
    print(f"{name} was added.")


def remove_student(students, student_keys):
    name = input("Enter the student's name to remove: ").strip()
    key = name.casefold()
    for saved_name in students:
        if saved_name.casefold() == key:
            students.remove(saved_name)
            student_keys.remove(key)
            print(f"{saved_name} was removed.")
            return
    print(f"{name} was not found.")


def search_students(students):
    query = input("Enter all or part of a name to search: ").strip().casefold()
    if not query:
        print("Search text cannot be empty.")
        return

    matches = [name for name in students if query in name.casefold()]
    if matches:
        print("Matching students:")
        for name in sorted(matches, key=str.casefold):
            print(f"- {name}")
    else:
        print("No matching students found.")


def display_students(students):
    ordered_students = sorted(students, key=str.casefold)
    print(f"\nTotal students: {len(ordered_students)}")
    if not ordered_students:
        print("No students in the records.")
        return

    for number, name in enumerate(ordered_students, start=1):
        print(f"{number}. {name}")


def show_menu():
    print("\nStudent Record Manager")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search students")
    print("4. Display all students")
    print("5. Exit")


def main():
    students = []
    student_keys = set()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(students, student_keys)
        elif choice == "2":
            remove_student(students, student_keys)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select a number from 1 to 5.")


if __name__ == "__main__":
    main()


# A list keeps an ordered collection and is useful when the program needs to display student names.
# A set stores unique values and is useful here for quickly checking whether a name has already been added.
# The list keeps the original spelling, while the set stores case-folded names for case-insensitive duplicate checks.
# When a student is removed, the name is removed from both collections so they stay in sync.
