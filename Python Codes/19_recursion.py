

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


"""
When we call this function with a positive integer, it will recursively call itself by 
decreasing the number.

Each function multiplies the number with the factorial of the number below it until 
it is equal to one. This recursive call can be explained in the following steps.

"""

