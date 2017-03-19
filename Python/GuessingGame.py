#  File: GuessingGame.py

#  Description: This program runs a guessing game to predict a user's number from 1 to 100 inclusive.

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447   

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: November 17, 2014

#  Date Last Modified: November 17, 2014

# This function returns the question to start the game
def Question():
    ques=input('Are you ready? (y/n):')
    if ques=='n':
        return 'Bye'
    elif ques=='y':
        print()
        return binarySearch()
    else:
        return Question()
# This function narrows the range to find the guessed number
def binarySearch():
    lo=1
    hi=100
    count = 1
    while (lo <= hi) and (count < 8):
        mid= (lo + hi) // 2
        print('Guess', count,':  The number you thought was', mid)
        guess= eval(input('Enter 1 if my guess was high, -1 if low, and 0 if correct:'))
        print()  
        if guess == 1:
            hi = mid - 1
            count += 1
        elif guess == -1:
            lo = mid + 1
            count += 1
        elif guess == 0:
            return 'Thank you for playing the Guessing Game.'
    return 'Either you guessed a number out of range or you had an incorrect entry.'
     
def main():
    # Write heading for the guessing game
    print('Guessing Game')
    print()
    print('Think of a number between 1 and 100 inclusive.')
    print('And I will guess what it is in 7 tries or less.')
    print()
    print(Question()) 
main()
