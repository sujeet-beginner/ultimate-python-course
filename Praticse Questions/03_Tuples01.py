'''
Write a program that:
1. Creates a tuple containing three city names.
2. Prints the second city.
3. Checks whether a particular city exists in the tuple.
4. Prints the number of elements.
5. Tries to change one element and observes what error Python produces.
Explain why the last operation fails.

'''
# 1. Creates a tuple containing three city names.
city = ("Pune", "Mumbai", "Latur")
print(city)

# 2. Prints the second city.
print(city[1])

# 3. Checks whether a particular city exists in the tuple.
print("Jalna" in city)

# 4. Prints the number of elements.
print(city)

# 4. Prints the number of elements.
city[1] = "Nashik"
print(city)      # The output will show error as tuples are immutable


