"""
Estimate: 20 minutes
Actual: 18 minutes
"""

from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

        print()
        name = input("Name: ")

    print()
    print("These are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
            f"worth ${guitar.cost:10,.2f}{vintage_string}"
        )


main()
