'''
Logan Lopez
CSC 122
Program 07a
'''

# Import the random class to use for generating random numbers
import random

# Accepts list of numbers, finds numbers greater than the input number
def larger_items(list, number):
    largerList = ""
    originalList = ""
    for i in list:
        originalList += str(i) + " "
        if (number < i):
            largerList += str(i) + " "
        
    print("Original list " + originalList)
    print("Items greater than " + str(number) +  ": " + largerList)
    return False

# Generates list of random numbers of a length 5-25
listLength = random.randrange(5,25)
numberList = []

# Create list of numbers to compare input number to
for i in range(0, listLength):
    number = random.randrange(1,20)
    numberList.append(number)

# Accept number to be compared to list
compare = int(input("Please enter a number to compare: "))

larger_items(numberList, compare)