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


def get_valid_score():
    score = int(input("Score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))

    return score
