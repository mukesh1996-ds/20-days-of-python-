# Data Types  -> this is how single line comments are used.

"""

In python what ever we store it will be a variable and the stored value will have a specifice datatype for that.
In python we will be mostly useing these types 

1. INT -> integer
2. FLOAT -> Float/ decimal value
3. STRING -> chatacter 

If you want to store a sequence of character in the list the use can use [] which directly represent the list which 
can hold any type of data.

If you want to fix the data and need not to change it then only use tuple it is represented driectly by () and It can
also store any type of data.

If you want to store data with specific name such as key and then its value then use dictionary and it is represented 
using {} where first you need to define a key and then its value -> {KEY:VALUE}


"""

a = complex(8, 2)
b = True
c = "Monu"
d = None
print(a)
print(b)
a1 = 9
print(a + a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))


# List 
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"), 9)
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True, "NAme2":"Mukeshs"}
print(dict1)