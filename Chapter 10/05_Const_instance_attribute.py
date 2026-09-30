class Employee:
    language = "Python"   # This is a Class Attribute
    salary =  120000


    def __init__(self, name, salary, langauge):   # dunder method which is automatically called
          self.name = name
          self.salary = salary
          self.language = langauge
          print("I am creating an object")

    @staticmethod   # no need of using self know : no property or object require 
    def greet():
        print("Good Morning!")

    def getInfo(self):
        print(f"The langauge is {self.language}. The salary is{self.salary}")


harry = Employee("Sujeet", 1300000, "Javascript")
harry.name = "Harry"
print(harry.name, harry.salary, harry.language)



#rohan = Employee()