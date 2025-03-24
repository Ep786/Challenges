#--------------------------------------------------------
# Name:      Conditional Statements (conditionalstatements.py)
# # Purpose:   To provide information about how conditional statements (if)
# #                         work in Python
# #
# # Author:    Emran
# # Created:   17-Mar-2025
# # Updated:   17-Mar-2025
#----------------------------------------------------------


temperature = int(input("What is the weather today?"))
if temperature < 10:
   print("It's cold outside. Wear a jacket")
elif temperature > 10 and temperature < 25:
    print("It's nice outside. Wear short-sleeves")
elif 25 < temperature:
    print("It's hot outside. Wear a shorts")
