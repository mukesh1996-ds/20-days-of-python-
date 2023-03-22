# A simple Python function

def fun():
    print("Welcome to My Python")

# Call a function
fun()


# Second project 

def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


# Third project

# some more functions
def is_prime(n):
	if n in [2, 3]:
		return True
	if (n == 1) or (n % 2 == 0):
		return False
	r = 3
	while r * r <= n:
		if n % r == 0:
			return False
		r += 2
	return True
print(is_prime(78), is_prime(79))


# Fourth Function 

# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)


# Fifth Function Default argument 

# Python program to demonstrate
# default arguments
def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10)


# Sixth Function Keyword arguments

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)


# Keyword arguments
student(firstname='World', lastname='Practice')
student(lastname='Practice', firstname='World')


# Seventh Function Default and positional arguments

def nameAge(name, age):
	print("Hi, I am", name)
	print("My age is ", age)


# You will get correct output because
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")

# Eighth Function Default and Arbitrary Keyword arguments

# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
	"""Function to check if the number is even or odd"""
	
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
print(evenOdd.__doc__)


# Multi function

# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
	s = 'I love GeeksforGeeks'
	
	def f2():
		print(s)
		
	f2()

# Driver's code
f1()


# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))


def square_value(num):
	"""This function returns the square
	value of the entered number"""
	return num**2


print(square_value(2))
print(square_value(-4))


# Here x is a new reference to same list lst
def myFun(x):
	x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def myFun(x):

	# After below line link of x with previous
	# object gets broken. A new object is assigned
	# to x.
	x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def myFun(x):

	# After below line link of x with previous
	# object gets broken. A new object is assigned
	# to x.
	x = 20


# Driver Code (Note that x is not modified
# after function call.
x = 10
myFun(x)
print(x)


def swap(x, y):
	temp = x
	x = y
	y = temp


# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)
