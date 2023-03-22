# Creating a dictionary

capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

"""
Keys are "Nepal", "Italy", "England"
Values are "Kathmandu", "Rome", "London"
"""
# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

"""
Add Elements to a Python Dictionary
We can add elements to a dictionary using the name of the dictionary with []. For example,
"""

capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ",capital_city)



"""
Change Value of Dictionary
We can also use [] to change the value associated with a particular key. For example,

"""

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)

student_id[112] = "Stan"

print("Updated Dictionary: ", student_id)

"""
Accessing Elements from Dictionary
In Python, we use the keys to access their corresponding values. For example,

"""

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print(student_id[111])  # prints Eric
print(student_id[113])  # prints Butters

"""
Removing elements from Dictionary
We use the del statement to remove an element from the dictionary. For example,

"""

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print("Initial Dictionary: ", student_id)

del student_id[111]

print("Updated Dictionary ", student_id)

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares) # prints True

print(2 not in squares) # prints True

# membership tests for key only not value
print(49 in squares) # prints false


# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares) # prints True

print(2 not in squares) # prints True

# membership tests for key only not value
print(49 in squares) # prints false
