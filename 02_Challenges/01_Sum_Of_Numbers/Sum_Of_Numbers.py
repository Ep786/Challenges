#--------------------------------------------------------
# Name:      Loops (Loops.py)
# # Purpose:   To provide information about Loops
# #                         work in Python
# #
# # Author:    Emran
# # Created:   26-Mar-2025
# # Updated:   26-Mar-2025
#----------------------------------------------------------


# Sum of Numbers using a For Loop
n = int(input("Enter a number: "))  # Get user input
sum = 0

for i in range(1, n + 1):  # Loop from 1 to n
    sum += i  # Add to sum

print("Sum =", sum)  # Print result
