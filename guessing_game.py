"""
@author: ramavishwanathan
"""


"""
The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
"""


"""
From the 'Introduction to Computer Science and Programming using Python" course offred by MITx via eDX.org
"""


low = 0
high = 100
guess = 50
print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number ",guess,"?")
    s = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if s=="c":
        print("Game Over. Your secret number was ",guess)
        break
    elif s == "h":
        high = guess
        guess = round((low + high)*0.5)
    elif s== "l":
        low = guess
        guess = round((low + high)*0.5)
    else:
        print("Sorry, I did not understand your input.")
