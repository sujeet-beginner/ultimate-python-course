# Write a __str__() method to print the vector as follows: 7i + 8j + 10k
 



class Vector:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        result = ""
        symbols = ["i", "j", "k"]

        for i in range(len(self.values)):
            result += str(self.values[i]) + symbols[i]

            if i < len(self.values) - 1:
                result += " + "

        return result


v = Vector([7, 8, 10])
print(v)
