class Contact:
    def __init__(self, first_name: str, last_name: str, phone_number: str):
        self.__first_name = first_name
        self.__last_name = last_name
        # self.name = {'__first_name': __first_name, '__last_name': __last_name}
        self.__phone_number = phone_number

    def set_first_name(self, first_name: str) -> None:
        self.__first_name = first_name
        # self.name['__first_name'] = __first_name

    def get_first_name(self) -> str:
        return self.__first_name
        # return self.name['__first_name']

    def get_last_name(self) -> str:
        return self.__last_name
        # return self.name['__last_name']

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_full_name(self) -> str:
        # return self.__first_name + ' ' + self.__last_name
        return f'{self.get_first_name()} {self.get_last_name()}'

    def call(self) -> None:
        print(f'Calling {self.get_phone_number()} ...')

if __name__ == '__main__':
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")

    my_test_contact = Contact(first_name, last_name, phone_number)

    print(my_test_contact.get_first_name())
    print(my_test_contact.get_last_name())
    print(my_test_contact.get_full_name())
    print(my_test_contact.get_phone_number())
    my_test_contact.call()

