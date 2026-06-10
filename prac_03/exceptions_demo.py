"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
# No longer need except ZeroDivisionError, because code stops that from happening beforehand.
print("Finished.")


# 1.  A ValueError will occur when typing something that cannot be converted into an integer such as "hello"
# 2.  A ZeroDivisionError will occur when the denominator is 0, because you cannot divide anything by 0.
# 3.  Yes, by checking if input == 0
