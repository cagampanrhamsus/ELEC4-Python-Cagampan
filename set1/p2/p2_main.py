# Name: Cagampan, Rhamsus Joshua C.
# Section: IV-BSIT C
# Activity: P2 - Student Utilities Main Program
# Date: November 23, 2026

from datetime import datetime
from student_utils import calculate_average, determine_pass_fail
import student_utils


def get_grades():
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


def main():
    grades = get_grades()
    generated_at = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    print("\nStudent Grade Report")
    print(f"Generated: {generated_at}")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest_grade(grades):.2f}")
    print(f"Lowest: {student_utils.get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_pass_fail(grades)}")


if __name__ == "__main__":
    main()
