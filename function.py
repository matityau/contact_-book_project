import json


CONTACTS = "contacts.json"



def load_contacts():
    with open(CONTACTS, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(CONTACTS, "w") as file:
        json.dump(contacts, file, indent=4)

def check_phone(phone,phone_exists = False):
    for name, info in contacts.items():
        if info.get('phone') == phone:
            phone_exists = True
            return phone_exists




