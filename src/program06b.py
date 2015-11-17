'''
Logan Lopez
CSC 122
Program 06b
'''

# Import the random class to use for generating random numbers
import random

# Ask for filename and number of lines to generate
fileName = input("Name of the file to output to: ")
randomNumber = int(input("Number of lines to output"))

# Open file with specified name for writing
file = open(fileName, 'w')
# Generate the specified number of random numbers and write them to the file
for i in range(0, randomNumber):
    number = str(random.randrange(1,500))
    file.write(number + '\n')