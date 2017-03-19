# File: Deal.py

# Description: This program runs a simulation of the game show
#              "Let's Make a Deal" to prove Marilyn vos Savant's advice.

# Student Name: Aasim Rajabali

# Student UT EID: afr447

# Course Name: CS 303E

# Unique Number: 57200

# Date Created: October 5th, 2014

# Date Last Modified: October 5th, 2014

import random

def main():
    #Prompt user to enter number of plays
    plays= eval(input('Enter number of times you want to play:'))
    win_count= 0
    heading= str(' Prize      Guess      View      New Guess ')
    print()
    print(heading)
    #Compute probabilities using randomization
    for i in range (plays):
        win= 0
        prize= random.randint(1,3)
        guess= random.randint(1,3)
        view= random.randint(1,3)
        while(view==prize or view==guess):
            view= random.randint(1,3)
            continue
        newGuess= random.randint(1,3)
        while(newGuess==view or newGuess==guess):
            newGuess= random.randint(1,3)
            continue
        if (newGuess==prize):
            win += 1
        if (win >= 1):
            win_count += 1
        print('  ', prize,'        ',guess,'       ',view,'          ',newGuess)
    switch= win_count / plays
    not_switch= 1 - switch
    #Compare results of switching and not switching
    print()
    print('Probability of winning if you switch:', format(switch, "2.2f"))
    print('Probability of winning if you do not switch:', format(not_switch, "2.2f"))
main()
