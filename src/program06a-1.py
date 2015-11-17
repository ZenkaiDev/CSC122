'''
Logan Lopez
CSC 122
Program 06a-1
'''

# Set condition for loop
loop = True

# Loop until loop is false
while (loop):
    
    # Get player name
    playerName = input("Player's name (empty string to quit)")
    
    # Exit loop if the name is empty
    if playerName == "":
        loop = False
    else:
        score = input("Score (>=0)")
        
        # Open file for appending
        file = open("golf.txt", 'a')
        
        # Write player name and score
        file.write(playerName + '\n')
        file.write(score + '\n')
        
        # Close file
        file.close()