# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Block a friend")
    print("5. Send a message to a friend")
    print("6. View all my messages")
    print("7. <- Log Out ")
    return input("Please Choose a number: ")

def editDetailsMenu():
    print("")
    print("1. Edit my username.")
    print("2. Edit my age.")
    print("3. <- Go back ")
    return input("Please Choose a number: ")
