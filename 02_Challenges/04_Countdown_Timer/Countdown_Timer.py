#--------------------------------------------------------
# Name:      Loops (Loops.py)
# # Purpose:   To provide information about Loops
# #                         work in Python
# #
# # Author:    Emran
# # Created:   26-Mar-2025
# # Updated:   26-Mar-2025
#----------------------------------------------------------


# Countdown Timer using While Loop + Break
count = 10

while count >= 1:
    print(count)
    user_input = input('Enter "stop" to cancel or press Enter: ')

    if user_input.lower() == "stop":
        print("Countdown stopped!")
        break  # Exit the loop

    count -= 1  # Decrement count

if count == 0:
    print("Countdown complete!")
