option = None
def add_contact():
    name = input("Enter the name of new contact: ")
    address = input(f"Enter the address of {name}: ")
    phone_no = input(f"Enter the phone number of {name}: ")
    info = [name, ", ", address, ", ", phone_no, "\n"]
    with open("contacts.txt", "a") as contacts:
        contacts.writelines(info)
def read_contacts():
    print("Name, Address, Phone Number")
    contacts_file = open("contacts.txt", 'r')
    print(contacts_file.readlines())
    print("Press Enter to continue...")
    input()
def remove_contact():
    pass
def intro():
    print("    /\\")
    print("   /  \\")
    print("  /----\\ Address Book Utility")
    print(" /      \\")
    print("/        \\")
    print("What would you like to do?")
    print("1. Add a contact")
    print("2. See a list of contacts")
    print("3. Exit")
    global option
    option = input()
    if option == "1":
        add_contact()
        intro()
    elif option == "2":
        read_contacts()
        intro()
    elif option == "3":
        import sys
        sys.exit()
    else:
        print("Invalid option.")
        intro()
intro()