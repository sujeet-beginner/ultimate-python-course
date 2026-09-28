'''
The game() function in a program lets a user play a game and return the score as an integer. You need to read a file 
"Hi-Score.txt" whic-h is either blank or contains the previous Hi-Score. You need to write a program to update the Hi-Score 
whenever the game () function breaks the Hi-Score 

'''

import random


def game():
    print("you are playing the game..")
    score = random.randint(1,62)
    #Fetch the hi-score
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score : {score}")
    if(score > hiscore):
        #write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score



game()