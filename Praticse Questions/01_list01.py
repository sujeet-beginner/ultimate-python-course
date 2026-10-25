'''
Create a list containing these marks: 72, 85, 91, 64, 78.

Write a program that:
1. Prints the first and last marks.
2. Prints the total number of marks.
3. Prints the highest and lowest marks.
4. Adds a new mark, 88, to the list.
5. Prints the updated list.


'''


marks = [72, 85, 91, 64, 78]

# 1. Prints the first and last marks.
print(marks[0])
print(marks[-1])

# 2. Prints the total number of marks.
print(sum(marks))

# 3. Prints the highest and lowest marks
print(min(marks))
print(max(marks))

# 4. Adds a new mark, 88, to the list.
marks.append(88)
print(marks)

# 5. Prints the updated list.
print(marks)