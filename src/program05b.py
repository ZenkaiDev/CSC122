'''
Logan Lopez
CSC 122
Program 05b
'''

# Import the random class to use to generate a number
import random

# Get random number
number = int(random.randrange(1,100))

# Set up variables
guessed = False
guesses = 0

# Loop until the guessed condition is true
while(not guessed):
    
    # Ask user for number input and convert to int
    guess = int(input("Guess? "))
    
    # Increment guess counter
    guesses += 1
    
    #Determine if input is higher, lower, or equal to random number
    if (guess < number ):
        print("Too low, try again")
    elif (guess > number):
        print("Too high, try again")
    else:
        print("You got it, took you " + str(guesses) + " guesses")
        # Fulfill condition to exit loop
        guessed = True
