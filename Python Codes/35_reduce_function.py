from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)

"""
In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements 
in the numbers list. The lambda function adds the two arguments x and y and returns the result. 
The reduce function applies the lambda function to the first two elements in the list (1 and 2), 
then applies the function to the result (3) and the next element (3),
and so on. The final result is the sum of all the elements in the list, which is 15.
"""