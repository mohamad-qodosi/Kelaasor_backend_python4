class BaseClass:
    @staticmethod
    def func1():
        print("BaseClass -> func1")

    @classmethod
    def run_all(cls):
        cls.func1()

class MyClass(BaseClass):
    @staticmethod
    def func1():
        print("MyClass -> func1")

MyClass.run_all()