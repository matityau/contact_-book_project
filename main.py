from function import *



if not os.path.exists("contacts.json"):
    with open("contacts.json", "w") as f:
        json.dump({}, f)

while True:
    print("""
                contact book program:
            For search contact press ------(1)
            For add a new contact press ---(2)
            For remove contacts press------(3)
            For edit contacts press -------(4)
            For view all contacts press----(5)
            For add a e-Mail press---------(6)
            
            For exit press ----------------(0)""")

    choose = input("Please choose your choice: ")

    if choose == "1":  # Search contact
        contacts = load_contacts()
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")
        person = first_name + " " + last_name

        if person in contacts:
            contact_info = contacts[person]
            print(f"Name: {person}")
            print(f"Phone: {contact_info.get('phone', 'N/A')}")
            print(f"Email: {contact_info.get('email', 'N/A')}")
        else:
            print(f"{person} does not exist")

    elif choose == "2":  # Add contact
        contacts = load_contacts()
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")
        person = first_name + " " + last_name

        if person in contacts:
            print("Contact already exists")
        else:
            phone = input("Please enter the contact phone: ")
            if check_phone(phone) == True:
                print(f"Phone {phone} already exists for {name}")

            else:
                contacts[person] = {"phone": phone, "email": ""}
                save_contacts(contacts)
                print(f"{person} added successfully")

    elif choose == "3":  # Remove contact
        contacts = load_contacts()
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")
        person = first_name + " " + last_name

        if person in contacts:
            del contacts[person]
            save_contacts(contacts)
            print(f"{person} removed successfully")
        else:
            print(f"{person} does not exist")

    elif choose == "4":  # Edit contact
        contacts = load_contacts()
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")
        person = first_name + " " + last_name

        if person in contacts:
            print(f"Current info for {person}:")
            print(f"Phone: {contacts[person].get('phone', 'N/A')}")
            print(f"Email: {contacts[person].get('email', 'N/A')}")

            new_phone = input("Enter new phone (press Enter to keep current): ")
            new_email = input("Enter new email (press Enter to keep current): ")

            if new_phone:
                contacts[person]["phone"] = new_phone
            if new_email:
                contacts[person]["email"] = new_email

            save_contacts(contacts)
            print(f"{person} updated successfully")
        else:
            print("Contact does not exist")

    elif choose == "5":  # View all contacts
        contacts = load_contacts()
        if contacts:
            print("\n--- All Contacts ---")
            for name, info in contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info.get('phone', 'N/A')}")
                print(f"Email: {info.get('email', 'N/A')}")
                print("-" * 20)
        else:
            print("No contacts found")

    elif choose == "6":  # Add email
        contacts = load_contacts()
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")
        person = first_name + " " + last_name

        if person in contacts:
            email = input("Please enter the email: ")
            contacts[person]["email"] = email
            save_contacts(contacts)
            print(f"Email added for {person}")
        else:
            print(f"{person} does not exist. Please add the contact first.")

    elif choose == "0":  # Exit
        print("Goodbye!")
        break