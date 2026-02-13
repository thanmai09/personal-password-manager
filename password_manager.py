def add_password():
    site = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{site} | {username} | {password}\n")

    print("Password saved successfully!")


def view_passwords():
    with open("passwords.txt", "r") as file:
        print("\nSaved Passwords:")
        print(file.read())


def search_password():
    search_site = input("Enter website to search: ")

    with open("passwords.txt", "r") as file:
        for line in file:
            if search_site.lower() in line.lower():
                print(line)


while True:
    print("\n1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        search_password()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
