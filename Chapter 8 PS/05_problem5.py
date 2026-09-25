'''
 Write a python fucntion to print first n lines of the following pattern :
 ***
 **
 *     for n = 3
 '''

def star(n):
     if(n == 0):
        return
     print("*" * n)
     star(n - 1)

star(5)