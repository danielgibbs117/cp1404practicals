minimum_password_length = 6


password = input("Password: ")


while len(password) < minimum_password_length:
    print(f"Password must be {minimum_password_length} characters or more")
    password = input("Password: ")


print("*" * len(password))
