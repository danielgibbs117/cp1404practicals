"""
Word Occurrences
Estimate:  40 minutes
Actual:    25 minutes
"""


def extract_name(email):
    username = email.split("@")[0]
    name_parts = username.split(".")
    name = " ".join(name_parts).title()
    return name


email_to_name = {}

email = input("Email: ")

while email != "":
    name = extract_name(email)

    confirmation = input(f"Is your name {name}? (Y/n) ")

    if confirmation.lower() not in ("", "y"):
        name = input("Name: ")

    email_to_name[email] = name

    email = input("Email: ")

print()

for email, name in email_to_name.items():
    print(f"{name} ({email})")
