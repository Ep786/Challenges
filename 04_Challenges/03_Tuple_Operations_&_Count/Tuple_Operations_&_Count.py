#--------------------------------------------------------
# Name:      Tuples  (Tuples.py
# # Purpose:   To provide information about Tuples
# #                         work in Python
# #
# # Author:    Emran
# # Created:   28-Mar-2025
# # Updated:   28-Mar-2025
#----------------------------------------------------------


# Creating a tuple with repeated words
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Asking the user for a word
user_input = input("Enter a fruit name: ")

# Counting how many times the word appears
count = fruits.count(user_input)

# Showing the result
print(f"'{user_input}' appears {count} times in the tuple.")
