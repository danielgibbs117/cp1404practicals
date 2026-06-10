def main():
    """Prints number of lines in each file by getting filename"""
    filename = input("Enter filename: ")

    while filename != "":
        try:
            number_of_lines = get_number_of_lines(filename)
            print(f"{filename} has {number_of_lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def get_number_of_lines(filename):
    """Returns number of lines in file"""
    number_of_lines = 0

    with open(filename, "r") as in_file:
        for line in in_file:
            number_of_lines += 1

    return number_of_lines


main()
