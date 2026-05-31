"""
CP1404/CP5632 - Practical
Program to determine score status
"""


import random


def main():
    score = float(input("Enter score: "))
    result = calculate_score(score)
    print(f"User score {score} is {result}")

    random_score = random.randint(0, 100)
    result = calculate_score(random_score)
    print(f"Random: {random_score} = {result}")


def calculate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
