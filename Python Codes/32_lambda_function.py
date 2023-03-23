str1 = 'I Love MY Country and all Indians are my neighbors' 

# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
# -> this function is an anonymous function which will captilize the string and also print it from the
# -> last
print(rev_upper(str1))


# Checking the difference between lambda function ans normal function 

def cube(y):
	return y*y*y


lambda_cube = lambda y: y*y*y


# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))


# Python Lambda with Multiple statements
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)

