# Write a class  vector represeting a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them 



class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])
        return Vector(result)

    def __mul__(self, other):
        result = 0
        for i in range(len(self.values)):
            result += self.values[i] * other.values[i]
        return result

    def __str__(self):
        return str(self.values)


# Creating two vectors
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Adding two vectors
print("Sum:", v1 + v2)

# Calculating dot product
print("Dot Product:", v1 * v2)
