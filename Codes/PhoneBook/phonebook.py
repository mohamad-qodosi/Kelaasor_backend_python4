from typing import List, Optional

from Codes.PhoneBook.contact import Contact

class PhoneBook1:
    def __init__(self):
        self.contacts : List[Contact] = []

    def add_contact(self, first_name: str, last_name: str, phone_number: str) -> None:
        new_contact = Contact(first_name, last_name, phone_number)
        self.contacts.append(new_contact)

    def find_contact_by_phone_number(self, phone_number: str) -> Optional[Contact]:
        for contact in self.contacts:
            if contact.get_phone_number() == phone_number:
                return contact
        return None

    def find_contact_by_first_name(self, first_name: str) -> Optional[Contact]:
        for contact in self.contacts:
            if contact.get_first_name() == first_name:
                return contact
        return None

    def find_contact_by_last_name(self, last_name: str) -> Optional[Contact]:
        for contact in self.contacts:
            if contact.get_last_name() == last_name:
                return contact
        return None

    def call_contact(self, phone_number: str) -> None:
        contact = self.find_contact_by_phone_number(phone_number)
        if contact:
            contact.call()
        else:
            print(f'No contact for phone number {phone_number}')




class PhoneBook2:
    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self, new_contact) -> None:
        self.contacts.append(new_contact)


if __name__ == '__main__':
    phonebook = PhoneBook1()
    phonebook.add_contact('John', 'Smith', '123456')
    phonebook.call_contact('123456')
    phonebook.call_contact('123457')

    phonebook = PhoneBook2()
    new_contact = Contact('John', 'Smith', '123456')
    phonebook.add_contact(new_contact)



