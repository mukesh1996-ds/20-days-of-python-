def f():

	# local variable
	s = "I love India"
	print(s)


# Driver code
f()


# This function uses global variable s
def f():
	print("Inside Function", s)

# Global scope
s = "I love You"
f()
print("Outside Function", s)


# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)


a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)
