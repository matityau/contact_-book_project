import csv
import json


CONTACTS = "contacts.json"
def enter_contact_details():
    first_name = input("Please enter the first name: ")
    last_name = input("Please enter the last name: ")
    person = first_name + " " + last_name
    return person

def load_contacts():
    with open(CONTACTS, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(CONTACTS, "w") as file:
        json.dump(contacts, file, indent=4)

def check_phone(phone,contacts):
    for name, info in contacts.items():
        if info.get('phone') == phone:
            return True

    return False

def print_contact(person, contact_info):
    print(f"Name: {person}")
    print(f"Phone: {contact_info.get('phone', '')}")
    print(f"Email: {contact_info.get('email', '')}")

def search_contact(contacts):
    person = enter_contact_details()
    if person in contacts:
        contact_info = contacts[person]
        print_contact(person, contact_info)
    else:
        print(f"{person} does not exist")

def add_new_contact(contacts):
    person = enter_contact_details()

    if person in contacts:
        print("Contact already exists")
    else:
        phone = input("Please enter the contact phone: ")
        check = check_phone(phone, contacts)
        if check:
            print(f'Phone {phone} already exists')

        else:
            contacts[person] = {"phone": phone, "email": ""}
            save_contacts(contacts)
            print(f"{person} added successfully")

def remove_contact(contacts):
    person = enter_contact_details()

    if person in contacts:
        del contacts[person]
        save_contacts(contacts)
        print(f"{person} removed successfully")
    else:
        print(f"{person} does not exist")

def edit_contact(contacts):
    person = enter_contact_details()

    if person in contacts:
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

def print_all_contacts(contacts):
    if contacts:
        print("\n--- All Contacts ---")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info.get('phone', 'N/A')}")
            print(f"Email: {info.get('email', 'N/A')}")
            print("-" * 20)
    else:
        print("No contacts found")

def edit_email(contacts):
    person = enter_contact_details()

    if person in contacts:
        email = input("Please enter the email: ")
        contacts[person]["email"] = email
        save_contacts(contacts)
        print(f"Email added for {person}")
    else:
        print(f"{person} does not exist. Please add the contact first.")

def export_contact_file(contacts):
        with open("contact.csv","w", newline="") as file:
            writer = csv.writer(file)

            for name, info in contacts.items():
                writer.writerow([name, info.get('phone'), info.get('email')])

        return "contacts.csv"




