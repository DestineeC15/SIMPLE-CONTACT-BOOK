# SIMPLE CONTACT BOOK

import json # importing json

CONTACTS_FILE = "contacts.json"

# add contact function
def add_contact(name, number):
    
    if name in contact_book and contact_book[name] == number: # Avoid adding duplicate contact
        print(f" This contact '{name}' already exists with this {number}.")
        return True
    elif number in contact_book.values(): # Avoid adding same number
        existing_name = None
        for key, value in contact_book.items():
            if value == number:
                existing_name = key
                break
        print(f" The number {number} already belongs to {existing_name}. Please enter a unique number.")
        return False
    
    elif name in contact_book: # Avoid adding same named contacts or overwriting contacts accidentally 
        print(f" The name '{name}' already exists with a different number {contact_book[name]}")

        while True:
            choice = input(" Do you want to overwrite this contact? Yes or No? ").strip().upper()

            if choice == "YES": # To uodate a contact
                contact_book[name] = number
                save_contacts(contact_book)
                print(f" The Contact '{name}' has been updated to {number}")
                print(contact_book)
                return True
            elif choice == "NO":
                print(" Operation has been cancelled. Please save the contact under a different contact name.")
                return False
            else:
                print(" Invalid choice! Please choose 'yes' or 'no'. ")
    else:
        contact_book[name] = number
        save_contacts(contact_book)
        print(" The contact has been succesfully added.")
        print(contact_book)
        return True


# Delete contact function
def delete_contact(name):
    if name not in contact_book:
        print(" This name does not exist in the contact book ")
        print(contact_book)
    else:
        contact_book.pop(name)
        print(" The contact has successfully been removed.")
        print(contact_book)

# Look up contact function
def lookup_contact(name):
    if name not in contact_book:
        print(" This contact does not exist")
    else:
        print(" Here is the contact's number.")
        print(contact_book[name])

# save contacts function
def save_contacts(data):

    try:
        with open(CONTACTS_FILE, 'w') as file_contacts:
            json.dump(data, file_contacts, indent = 4)
            print(" Contacts have been saved successfully! ")
    except Exception as e:
        print(f" Error saving contacts, {e} ")

# load contacts function
def load_contacts():

    try:
        with open(CONTACTS_FILE, 'r') as file_contacts:
            return json.load(file_contacts)
    except FileNotFoundError: # <--- ADD THIS BLOCK
        print(" Contact file not found. Starting with an empty contact book.")
        return {}
    except json.JSONDecodeError:
        print(" There was an error reading file. Starting with an empty file.")
        return {}
    
contact_book = load_contacts()


while True:
    try:
        action = int(input("Please choose action to perform. 1 = add contact, 2 = delete contact, 3 = lookup contact, 4 = exit "))
        
        match action:
            case 1:
                while True:
                    contact_name = input(" Please enter the contact's full name ").strip().upper()

                    while True:
                        contact_number = input(" Please enter the contact's number ").strip()
                        if contact_number.isdigit():
                            break
                        else:
                            print(" Invalid format! Please enter only digits.") 

                    if add_contact(contact_name, contact_number):
                        break
            case 2:
                delete_contact_name = input(" Please enter contact name to delete from contact book ").strip().upper()
                delete_contact(delete_contact_name)
            case 3:
                find_contact = input(" Please enter contact name that you would like to lookup ").strip().upper()
                lookup_contact(find_contact)
            case 4:
                print("Exiting. Thank you for using the contact book.")
                break
            case _:
                print("Invalid action!")

    except ValueError:
        print("Choose a valid action. 1, 2, 3 or 4. ")


