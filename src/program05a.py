# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Logan"
__date__ = "$Oct 28, 2015 6:49:55 PM$"
def calc_average(scores = []):
    avg = 0
    for score in scores:
        avg = avg + score
    avg = avg / 5 
    return avg

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

score = [0] * 5    
for x in range(1, 6):
    score[x - 1] = int(input("Score " + str(x) + "? "))
    print("That's a(n) " + determine_grade(score[x - 1]))
avg = str(calc_average(score))
print("Your average score was: " + avg + " which is a(n) " + determine_grade(avg))