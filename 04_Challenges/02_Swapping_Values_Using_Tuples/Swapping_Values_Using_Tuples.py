#--------------------------------------------------------
# Name:      Tuples  (Tuples.py
# # Purpose:   To provide information about Tuples
# #                         work in Python
# #
# # Author:    Emran
# # Created:   28-Mar-2025
# # Updated:   28-Mar-2025
#----------------------------------------------------------


# Asking for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Putting numbers in a tuple
numbers = (num1, num2)

# Swapping values
num1, num2 = num2, num1

# Showing the swapped numbers
print("Swapped values:", (num1, num2))