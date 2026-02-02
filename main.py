from function import *
from uli import  *
import os


if not os.path.exists("contacts.json"):
    with open("contacts.json", "w") as f:
        json.dump({}, f)

contacts = load_contacts()
while True:

    print(uli())

    choose = input("Please choose your choice: ")

    if choose == "1":
        search_contact(contacts)

    elif choose == "2":
        add_new_contact(contacts)

    elif choose == "3":
        remove_contact(contacts)

    elif choose == "4":
        edit_contact(contacts)

    elif choose == "5":
       print_all_contacts(contacts)

    elif choose == "6":
        edit_email(contacts)

    elif choose == "7":
        export_contact_file(contacts)

    elif choose == "0":
        print("Goodbye!")
        break