class Person:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"{self.__name}"


class Employee(Person):
    __number_of_instances = 0

    def __init__(self, name):
        super().__init__(name)
        self.__id = Employee.__number_of_instances
        # self.__class__.__number_of_instances = self.__class__.__number_of_instances + 1
        Employee.__number_of_instances += 1

    @staticmethod
    def get_number_of_instances():
        return Employee.__number_of_instances

    @staticmethod
    def get_id_string(id):
        return f"{id:05d}"

    def __str__(self):
        return super().__str__() + ': ' + self.get_id_string(self.__id)


if __name__ == "__main__":
    emps = [Employee("Mohammad"), Employee("Taha"),
            Employee("Amir Reza"), Employee("Alireza"),
            Employee("Danial"), Employee("Dibadokht"),
            Employee("Atra"), Employee("Sana")]
    for emp in emps:
        print(emp)
