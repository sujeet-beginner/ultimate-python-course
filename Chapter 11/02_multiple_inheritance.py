# Multiple inheritance occurs when the child inherits from more than one parent classes


class Employee:
    comapany = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.comapany}")


class Coder:
    langauge = "Python"
    def printLanguages(self):
        print(f"Out of all the langauge here is your langauge: {self.langauge}")




class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with{self.langauge} langauge")




a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()