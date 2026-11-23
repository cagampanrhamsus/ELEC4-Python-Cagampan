# Name: Cagampan, Rhamsus Joshua C.
# Section: IV-BSIT C
# Activity: P2 - Student Utilities Module
# Date: November 23, 2026

"""Reusable functions for working with student grades."""


def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_pass_fail(grades):
    return "Passed" if calculate_average(grades) >= 75 else "Failed"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)
