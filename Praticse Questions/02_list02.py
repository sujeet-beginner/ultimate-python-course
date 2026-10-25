'''
Write code to:
1. Replace "banana" with "grapes".
2. Add "watermelon" to the end.
3. Remove "mango".
4. Print the final list.
5. Check whether "apple" exists in the list

'''

fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

# 1. Replace "banana" with "grapes".
fruits[1] = "grapes"
print(fruits)

# 2. Add "watermelon" to the end.
fruits.append("Watermelon")
print(fruits)

# 3. Remove "mango".
fruits.pop(2)
print(fruits)

# 4. Print the final list.
print(fruits)

# Check whether "apple" exists in the list
print("apple" in fruits)