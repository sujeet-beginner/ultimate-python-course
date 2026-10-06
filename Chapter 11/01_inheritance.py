# Inheritance is a way of creating a new class from the  exisiting class


class Employee:
    comapany = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")



# class Programmer:
#    company = "ITC Company"
#    def show(self):
#        print(f"The name is {self.name} and the salary is {self.salary}")

#    def showLangauge(self):
#        print(f"The name is {self.name} and he is good with {self.langauge} language")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with{self.langauge}langauge")




a = Employee()
b = Programmer()

print(a.comapany, b.company)