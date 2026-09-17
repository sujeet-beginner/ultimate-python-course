# A spam comment is defined as a text containing following keywords :
#"Make a lot of money", "buy now", "Subscribe these","click me".  write a program to detect these spams

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscribe now"
p4 = "click this"

message = input("Enter your comment : " )

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("These comment is a spam")

else :
    print("These comment is not a spam !")