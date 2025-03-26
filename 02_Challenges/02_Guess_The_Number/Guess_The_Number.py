#--------------------------------------------------------
# Name:      Loops (Loops.py)
# # Purpose:   To provide information about Loops
# #                         work in Python
# #
# # Author:    Emran
# # Created:   26-Mar-2025
# # Updated:   26-Mar-2025
#----------------------------------------------------------


import random  # Import random module

random_number = random.randint(1, 10)  # Generate random number
guess = None

while guess != random_number:
    guess = int(input("Guess the number: "))  # Get user input
    if guess != random_number:
        print("Wrong, try again!")

print("Correct! 🎉")  # Correct guess message
