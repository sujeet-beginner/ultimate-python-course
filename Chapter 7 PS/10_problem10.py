# WAP to print multiplication table of n using for loops in reversed order
n = int(input("Enter a number:"))

print("table of ",n)
for i in range(10):
    print(n*(10-i))
