# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))


"""
In the above example, the lambda function lambda x: x * 2 is used to double each element in the numbers list. 
The map function applies the lambda function to each element in the list and returns a new list containing 
the doubled numbers.
"""

