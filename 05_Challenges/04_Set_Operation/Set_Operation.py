# --------------------------------------------------------
# Name:      Sets  (Sets.py
# # Purpose:   To provide information about Sets
# #                         work in Python
# #
# # Author:    Emran
# # Created:   8-Apr-2025
# # Updated:   8-Apr-2025
# ----------------------------------------------------------


# Create the sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Find the union
union = set1.union(set2)
# Alternate way: union = set1 | set2

# Find the intersection
intersection = set1.intersection(set2)
# Alternate way: intersection = set1 & set2

# Find the difference
difference = set1.difference(set2)
# Alternate way: difference = set1 - set2

# Print the results
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)