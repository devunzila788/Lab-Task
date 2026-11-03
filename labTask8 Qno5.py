def check_password(password):
    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(not char.isalnum() for char in password)):
        print("Password is valid")
    else:
        print("Password is invalid")
password = input("Enter your password: ")
check_password(password)