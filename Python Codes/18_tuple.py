# Creating a tuple 

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)




text = ("Hello World!", "Hello World")
print(type(text))

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(type(my_tuple))

my_tuple = ("mouse", 8, 4, 6, 1, 2, 3)
print(type(my_tuple))


# Positive Indexing 

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(letters[0])   # prints "p" 
print(letters[5])   # prints "a"

# Negative indexing

# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1])   # prints 'z' 
print(letters[-3])   # prints 'm'

# Sliceing 

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')

# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')

# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3

"""
Iterating through a Tuple in Python
We can use the for loop to iterate over the elements of a tuple. For example,
"""
languages = ('Python', 'Swift', 'C++')

# iterating through the tuple
for language in languages:
    print(language)


"""
Check if an Item Exists in the Python Tuple
We use the in keyword to check if an item exists in the tuple or not. For example,
"""
languages = ('Python', 'Swift', 'C++')

print('C' in languages)    # False
print('Python' in languages)    # True


