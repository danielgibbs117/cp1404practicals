"""
Word Occurrences
Estimate:  60 minutes
Actual:    77 minutes
"""

import csv

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    records = load_records(FILENAME)
    champion_to_wins, countries = process_records(records)
    display_results(champion_to_wins, countries)


def load_records(filename):
    records = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)

        for row in reader:
            records.append(row)

    return records


def process_records(records):
    champion_to_wins = {}
    countries = set()

    for record in records:
        champion = record[CHAMPION_INDEX]
        country = record[COUNTRY_INDEX]

        countries.add(country)

        if champion in champion_to_wins:
            champion_to_wins[champion] += 1
        else:
            champion_to_wins[champion] = 1

    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    print("Wimbledon Champions:")

    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()

