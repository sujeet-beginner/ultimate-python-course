age = int(input("Enter Your Age :"))

if(age >= 18) :
    print("You are above the age of consent")
    print("Good for you !")

elif(age < 0) :
    print("you are entering an invlaid negative age")

elif(age == 0) :
    print("you are entering 0 which is not an valid age")


else :
    print("You are below the age consent ")19