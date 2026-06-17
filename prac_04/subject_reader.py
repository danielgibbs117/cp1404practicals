"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_data(FILENAME)
    display_subject_details(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        subject = [parts[0], parts[1], int(parts[2])]
        subject_data.append(subject)
        print(subject)  # See if that worked
        print("----------")
    input_file.close()
    return subject_data


def display_subject_details(subject_data):
    for subject in subject_data:
        subject_code = subject[0]
        lecturer = subject[1]
        students = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {students} students")


main()

