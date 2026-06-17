import random

numbers_per_line = 6
minimum_number = 1
maximum_number = 45

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []

    while len(quick_pick) < numbers_per_line:
        number = random.randint(minimum_number, maximum_number)

        if number not in quick_pick:
            quick_pick.append(number)

        quick_pick.sort()

        for number in quick_pick:
            print(f"{number:2}", end=" ")

        print()
