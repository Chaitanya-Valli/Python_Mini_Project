print("*"*6+"Cntact Book Using Function"+"*"*6)
print("1. Add Contact")
print("2. Search Contact")
print("3. Update Contact")
print("4. Delete Contact")
print("5. View Contacts")
print("6. Exit")

contacts={}
def add_contact():
    name=input("Enter Contact Name: ").strip()
    if name in contacts:
        print(f" {name} Already Exist")
    else:
        mobile_num=input("Enter Mobile Number: ").strip()
        contacts[name]=mobile_num
        print("Contact added successfully")

def search_contact():
    name=input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Found {name}-{contacts[name]}")
    else:
        print(f" Contact {name} not found")

def update_contact():
    name=input("Enter contact name to search: ").strip()
    if name in contacts:
        new_number=input("Enter new phone number: ").strip()
        contacts[name]=new_number
        print(f"Contact {name} updated successfully")
    else:
        print(f"Contact {name} not exist")

def delete_contact():
    name=input("Enter contact name to search: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully")
    else:
        print(f"Contact {name} not exist")

def view_contacts():
    if not contacts:
        print("No contacts")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")

choice = input("Choose an option (1-6): ").strip()
if choice == '1':
    add_contact()
elif choice == '2':
    search_contact()
elif choice == '3':
    update_contact()
elif choice == '4':
    delete_contact()
elif choice == '5':
    view_contacts()
elif choice == '6':
    print("Exiting Contacts.")
else:
    print("Invalid choice! Please enter a number between 1 and 6.")
