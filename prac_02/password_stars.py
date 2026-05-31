minimum_password_length = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print(f"Password must be {minimum_password_length} characters or more")
        password = input("Password: ")
    return password


main()
