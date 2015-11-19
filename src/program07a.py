'''
Logan Lopez
CSC 122
Program 07a
'''

# Import the random class to use for generating random numbers
import random

# Check to see if value exists in list
def in_list(list, val):
    count = list.count(val)
    if (count > 0):
        return True
    else:
        return False

# Init list so we can use len in while loop
list = []

# Loop until length of list is 9
while (len(list) < 9):
    
    # Generate random number
    number = random.randrange(0,9)
    
    # Generate a number until it isn't a duplicate
    while (in_list(list, number) != False):
        number = random.randrange(0,9)
    # Append the number to the list
    list.append(number)

# Init output
output = ""

# Loop through list and append value to output
for i in list:
    output += str(i) + ""
    
# Output list
print(output)