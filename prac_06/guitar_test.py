"""
Estimate: 10 minutes
Actual: 15 minutes
"""

import datetime

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 0)

    current_year = datetime.datetime.now().year

    print(
        f"{gibson.name} get_age() - "
        f"Expected {current_year - gibson.year}. Got {gibson.get_age()}"
    )
    print(
        f"{another_guitar.name} get_age() - "
        f"Expected {current_year - another_guitar.year}. "
        f"Got {another_guitar.get_age()}"
    )

    print(
        f"{gibson.name} is_vintage() - "
        f"Expected True. Got {gibson.is_vintage()}"
    )
    print(
        f"{another_guitar.name} is_vintage() - "
        f"Expected False. Got {another_guitar.is_vintage()}"
    )


main()
