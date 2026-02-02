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




