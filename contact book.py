#####################################################################
# ---------------------CodeSoft Internship--------------------------#
# Created: 5/12/2023 9:25:34 PM                                     #
# Author: Salah Eldeen Mohamed Hemdan                               #
# Project: Contact Book                                             #
#####################################################################

############################ Import Section ################################
import tkinter as tk
from tkinter import simpledialog

############################ Function Section ################################
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)

    def view_contacts(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
                results.append(contact)
        return results

    def update_contact(self, old_name, new_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact['Name'] == old_name:
                contact['Name'] = new_name
                contact['Phone'] = new_phone
                contact['Email'] = new_email
                contact['Address'] = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['Name'] == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_term)
            print("\nSearch Results:")
            for result in results:
                print(result)

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            new_address = input("Enter the new address: ")
            contact_book.update_contact(old_name, new_name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

############################ Program Section ################################
if __name__ == "__main__":
    main()
