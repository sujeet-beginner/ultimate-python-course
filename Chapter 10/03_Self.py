# Self refers to the instance of the class. It is automatically passed with a fucntion call from an object.


class Employee:
    language = "Python"   # This is a Class Attribute
    salary =  120000

    @staticmethod
    def greet():
        print("Good Morning!")

    def getInfo(self):
        print(f"The langauge is {self.language}. The salary is{self.salary}")


harry = Employee()
harry.language = "Javascript"  # This is an instance attribute
harry.getInfo()
#Employee.getInfo(harry)