
# if elif and else example 


# Taking the input from the user 

daysnumber = int(input("Enter the week number:- "))

if daysnumber == 0:
    print("Invalid days number, user input is {}".format(daysnumber))
elif daysnumber == 1:
    print("The day is Monday and have a great day, user input is {}".format(daysnumber))
elif daysnumber == 2:
    print("The day is Tuesday and have a great day, user input is {}".format(daysnumber))
elif daysnumber == 3:
    print("The day is Wednesday and have a great day, user input is {}".format(daysnumber))
elif daysnumber == 4:
    print("The day is Thursday and have a great day, user input is {}".format(daysnumber))
elif daysnumber == 5:
    print("The day is Friday and have a great day, user input is {}".format(daysnumber))
elif daysnumber == 6:
    print("The day is Saturday and have a great day, user input is {}".format(daysnumber))
elif daysnumber == 7:
    print("The day is Sunday and have a great day, user input is {}".format(daysnumber))
else:
    print("Invalid resonse from the user {}".format(daysnumber))



"""
Note: The condition will check everything using logical operator and perfrom the action 
"""


