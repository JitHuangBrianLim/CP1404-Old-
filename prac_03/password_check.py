MINIMUM_PASSWORD_LENGTH = 5

def main():
    password = get_password(MINIMUM_PASSWORD_LENGTH)
    hide_password(password)

def get_password(MINIMUM_PASSWORD_LENGTH):
    password = input("Enter password: ")

    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password too short. Re-enter password.")
        password = input("Enter password: ")
    return password

def hide_password(password):
    for i in range(0, len(password)):
        print("*", end='')

main()