import random

'''
1  for snake
-1 for water
0  for for gun

'''

computer  = random.choice([-1, 0, 1])
youstr    = input("Enter your choice : ")
youDict   = {"s": 1, "w": -1, "g": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"you choose {reversedDict[you]}\nComputer choose {reversedDict[computer]}")


if(computer == you):
    print("Its is a draw")

else:

    '''
    if((computer - you == -1) or (computer - you) == 2):
        print("you loose!)
    else:
        print("you  win!")


    '''
    if(computer == -1 and you == 1):
        print("you win!")

    elif(computer == -1 and you == 0):
        print("you loose!")

    elif(computer ==  1 and you == -1):
        print("you loose!")

    elif(computer == 1 and you == 0):
        print("you loose!")

    elif(computer == 0 and you == -1):
        print("you loose!")

    elif(computer == 0 and you == 1):
        print("you loose!")

    else:
        print("Something went wrong!")



