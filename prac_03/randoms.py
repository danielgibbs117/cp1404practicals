import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Line 1
# I saw 7 on line 1.
# The smallest number I could have seen is 5, the biggest would be 20.


# Line 2
# I saw 3 on line 2.
# The smallest number I could have seen is 3, the biggest would be 9.
# No, it could not produce a 4 because it goes up in increments of 2 starting from 3.


# Line 3
# I saw 3.8073358033281677 on line 3.
# The smallest number I could have seen is 2.5, the biggest would be 5.5.

print(random.randint(1, 100))
