#--------------------------------------------------------
# Name:      Conditional Statements (conditionalstatements.py)
# # Purpose:   To provide information about how conditional statements (if)
# #                         work in Python
# #
# # Author:    Emran
# # Created:   20-Mar-2025
# # Updated:   20-Mar-2025
#----------------------------------------------------------



VotElgChk = int(input("How old are you?"))
if VotElgChk > 17:
    print("You are eligible")
elif VotElgChk < 18:
    print("You are not eligible")
    print("Sorry")