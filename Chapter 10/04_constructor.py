# Self refers to the instance of the class. It is automatically passed with a fucntion call from an object.


class Employee:
    language = "Python"   # This is a Class Attribute
    salary =  120000


    def __init__(self):   # dunder method which is automatically called
          print("I am creating an object")

    @staticmethod   # no need of using self know : no property or object require 
    def greet():
        print("Good Morning!")

    def getInfo(self):
        print(f"The langauge is {self.language}. The salary is{self.salary}")


harry = Employee()
harry.name = "Harry"
print(harry.name, harry.salary)
#Employee.getInfo(harry)


rohan = Employee()