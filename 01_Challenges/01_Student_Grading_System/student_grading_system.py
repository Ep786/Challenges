#---------------------------------------------------------
# Name:      Conditional Statements (conditionalstatements.py)
# Purpose:   To provide information about how conditional statements (if)
#                         work in Python
#
# Author:    Emran
# Created:   26-Feb-2025
# Updated:   26-Feb-2025
#----------------------------------------------------------


print("Welcome to the student grading system")
myScore = int(input("What is your score?: "))
# Basic if statement
if myScore >= 90 and myScore <= 100:
    print("Your grade is A")
    print("Congratulations!")
# Using 'elif' in a conditional
elif myScore >= 80 and myScore <= 89:
    print("Your grade is B")
    print("Congratulations!")
elif myScore >= 70 and myScore <= 79:
    print("Your grade is C")
    print("Good Job")
# Using 'and' in conditional chain
elif myScore >= 60 and myScore <= 69:
    print("Your grade is D")
    print("Nice")
elif myScore < 60:
    print("Your grade is F")
    print("Work harder next time!")
else:
    print("Your input is wrong")