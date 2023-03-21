
# Getting input from the users 


user1 = input("Enter the number:- ")
print("The numnber entered by the user1 is {}".format(user1))
print(type(user1)) # type(val) is used to check the datatype of the variable

"""
imaigne that user1 has entered 33 in the terminal, we all know that its a integer but our Python don't know that 
so it will consider everything as string i.e. str only. 

TO OVER COME WE CAN USE TYPECASTING.

"""

# By default initilizing the TYPECASTING/conversion 
user2= int(input("Enter the number:- "))
print("The numnber entered by the user1 is {}".format(user2))
print(type(user2)) # type(val) is used to check the datatype of the variable
