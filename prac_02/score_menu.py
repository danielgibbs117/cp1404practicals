"""
print menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        print invalid input error message
    print menu
    get choice
<do final thing, if needed>
"""


def print_menu():
    print("(G)et valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    score = int(input("Score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))

    return score


def calculate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_asterisks(score: int):
    print("*" * score)
