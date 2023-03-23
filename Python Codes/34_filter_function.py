# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))

"""
In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers list and return 
only the even numbers. The filter function 
applies the lambda function to each element in the list and returns a new list containing only the even numbers.

"""