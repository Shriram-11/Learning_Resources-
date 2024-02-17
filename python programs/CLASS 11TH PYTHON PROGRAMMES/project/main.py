import csv


def load_contacts():
    contacts = []
    try:
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                contacts.append(
                    {'name': row[0], 'phone_number': row[1], 'address': row[2]})
    except FileNotFoundError:
        # If file doesn't exist, return an empty list
        pass
    return contacts


def save_contacts(contacts):
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow(
                [contact['name'], contact['phone_number'], contact['address']])


def print_contacts(contacts):
    print("\nContacts:")
    print("----------------------------------------------------")
    print("| {:<20} | {:<15} | {:<30} |".format(
        'Name', 'Phone Number', 'Address'))
    print("----------------------------------------------------")
    for contact in contacts:
        print("| {:<20} | {:<15} | {:<30} |".format(
            contact['name'], contact['phone_number'], contact['address']))
    print("----------------------------------------------------")


def search_contact_by_name(contacts, name):
    found_contacts = [
        contact for contact in contacts if name.lower() in contact['name'].lower()]
    return found_contacts


def add_new_contact(contacts):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    address = input("Enter address: ")
    new_contact = {'name': name,
                   'phone_number': phone_number, 'address': address}
    contacts.append(new_contact)
    save_contacts([new_contact])  # Saving only the new contact
    print("Contact added successfully.")


def main():
    try:
        with open('contacts.csv', 'r') as file:
            pass
    except FileNotFoundError:
        # If file doesn't exist, create an empty file and write the header
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'phone_number', 'address'])

    contacts = load_contacts()
    while True:
        print("\nOptions:")
        print("1. View contacts")
        print("2. Search contact by name")
        print("3. Add new contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print_contacts(contacts)
        elif choice == '2':
            name = input("Enter name to search: ")
            found_contacts = search_contact_by_name(contacts, name)
            if found_contacts:
                print_contacts(found_contacts)
            else:
                print("No contacts found with that name.")
        elif choice == '3':
            add_new_contact(contacts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
