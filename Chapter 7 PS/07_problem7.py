# WAP to print the following star patter  :
'''
For n = 3
  *
 ***
*****

'''

n  = int(input("Enter the number :"))
for i in range(1, n + 1):
    print(" "* (n - i), end = " ")      # print usually take to the new line ; here what end does is that : it doesnt takes us to the new line
    print("*"* (2*i-1), end = "")
    print("")