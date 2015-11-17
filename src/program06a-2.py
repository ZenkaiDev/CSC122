'''
Logan Lopez
CSC 122
Program 06a-2
'''
# Open file for reading
file = open("golf.txt", 'r')

# Get list of lines in file
list = file.read().splitlines()

# Get number of lines in file
groups = int(len(list))

# Iterate through list in steps of 2 (name, score)
for i in range(0, groups, 2):
    # Get player name and score
    playerName = list[i]
    score = list[i + 1]
    # Output 
    print(playerName + " scored a " + score)