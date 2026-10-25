class student :
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def update_marks(self, new_marks):
        self.marks = new_marks
student1 = student("Sujeet", 100)
student1.update_marks(90)
print(student1.marks)