#--------------------------------------------------------
# Name:      Conditional Statements (conditionalstatements.py)
# # Purpose:   To provide information about how conditional statements (if)
# #                         work in Python
# #
# # Author:    Emran
# # Created:   20-Mar-2025
# # Updated:   20-Mar-2025
#----------------------------------------------------------


DayWeekRec = (input("What day is it?"))
if DayWeekRec == "Monday":
    print("Start your day with workout!")
elif DayWeekRec == "Tuesday":
    print("It's a great day to read a book!")
elif DayWeekRec == "Wednesday":
    print("Mid-week movie night!")
elif DayWeekRec == "Thursday":
    print("Try a new recipe!")
elif DayWeekRec == "Friday":
    print("Relax and enjoy the weekend!")
elif DayWeekRec == "Saturday":
    print("Go for a hike!")
elif DayWeekRec == "Sunday":
    print("Prepare for the week ahead with some self care!")
else:
    print("Invaled!")