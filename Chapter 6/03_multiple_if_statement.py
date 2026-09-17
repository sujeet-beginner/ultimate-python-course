age = int(input("Enter Your Age :"))

# If statement  no : 1
if(a % 2 == 0) :
    print(" a is even ")

# End of  If statement  no : 1

# # If statement  no : 2
if(age >= 18) :
    print("You are above the age of consent")
    print("Good for you !")

elif(age < 0) :
    print("you are entering an invlaid negative age")

elif(age == 0) :
    print("you are entering 0 which is not an valid age")


else :
    print("You are below the age consent ")