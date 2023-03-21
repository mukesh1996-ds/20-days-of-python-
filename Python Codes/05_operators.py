"""
Operators are the mathematical function that will help us to perfrom mathematical operations. In python we are having 
multiple different types of operators:

1. Arithematic operators: To perform all the mathematical operations such as addition, subtraction, multiplication,
etc.

2. Relational operators OR comparision operators: It is used to check the releation between two similar datatypes for example:
 if a user enter 10 in the consule and b user enter 20 in the consule to check which number is big and which number is small we 
 use this comparision operators. 

3. Logical Operators: These operators are used when we want to compare values logically. There are Logical AND, Logical OR, Logical NOT

4. Bitwise operators : In Python, bitwise operators are used to perform bitwise calculations on integers. The integers are first converted
 into binary and then operations are performed on each bit or corresponding pair of bits, hence the name bitwise operators. The result is 
 then returned in decimal format.

5. Assignment operators: Assignment operators are used to assign values to variables 


"""
# --> Arithematic Operators <--

print("Addition of two numbers:-", 5+6)
print("Subtraction of two numbers:-",15-6)
print("Multiplication of two numbers:-",15*6)
print("Division of two numbers:-",15/6)
print("Floor division of two numbers:-",15//6)
print("Modulus of two numbers:-",5%3)
print("Exponential OR power of 2:-",2**4)

# --> Relational operators OR comparision operators <--

user1 = 10  
user2 = 20

print(user1<user2, "user1 is big")
print(user1>user2, "user2 is big")
print(user1==user2, "Not equal")
print(user1<=user2, "user1 is big")
print(user1>=user2, "user2 is big")
print(user1 != user2)


# --> Logical operators <--

a = 10
b = 10
c = -10

if a > 0 and b > 0:
	print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
	print("The numbers are greater than 0")
else:
	print("Atleast one number is not greater than 0")


# --> Bitwise Operator <--

a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)

# Print bitwise OR operation
print("a | b =", a | b)

# Print bitwise NOT operation
print("~a =", ~a)

# print bitwise XOR operation
print("a ^ b =", a ^ b)


# --> Assignment Operator <--

a = 3
b = 5

c = a + b

# Output
print(c)
