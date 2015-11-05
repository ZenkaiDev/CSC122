'''
Logan Lopez
CSC 122
Program 05a
'''

#  Calculate average of array of scores
def calc_average(scores = []):
    avg = 0
    for score in scores:
        avg = avg + score
    avg = avg / len(scores) 
    return avg

# Determine what letter grade the score falls into
def determine_grade(score):
    score = float(score)
    if (score >= 90):
        return "A"
    elif (score >= 80):
        return "B"
    elif (score >= 70):
        return "C"
    elif (score >= 60):
        return "D"
    else:
        return "F"

# Create empty array of length 5
score = [0] * 5   

# Loop 5 times to fill array with scores
for x in range(1, 6):
    score[x - 1] = int(input("Score " + str(x) + "? "))
    print("That's a(n) " + determine_grade(score[x - 1]))
    
# Pass score into average function
avg = str(calc_average(score))

# Output average score and the letter grade for that score
print("Your average score was: " + avg + " which is a(n) " + determine_grade(avg))