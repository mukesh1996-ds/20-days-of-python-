# Python Notes in details 

What is Programming ?

Programming is a way for us to tell computers what to do. Computer is a very dumb machine and it only does what we tell it to do. Hence we learn programming and tell computers to do what we are very slow at - computation. If I ask you to calculate 5+6, you will immediately say 11. How about 23453453 X 56456?

You will start searching for a calculator or jump to a new tab to calculate the same.

What is Python?
* Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
* Python is an interpreted and a high-level programming language.
* It was created by Guido Van Rossum in 1989.

Features of Python

* Python is simple and easy to understand.
* It is Interpreted and platform-independent which makes debugging very easy.
* Python is an open-source programming language.
* Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.
* It is possible to integrate other programming languages within python.

What is Python used for

* Python is used in Data Visualization to create plots and graphical representations.
* Python helps in Data Analytics to analyze and understand raw data for insights and trends.
* It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
* It is used to create web applications.
* It can be used to handle databases.
* It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.

Example1: You can see how to write your first program to print "Hello World" 

Here are few of the mini project that can we done with the help of Python and many more coming soon..
 link for all the mini projects: https://replit.com/@codewithharry/02-Day2-Application-of-Python#5.%20Snake%20Game/Snake.py


## Modules and pip in Python!

Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:

1. Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.

2. External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

The pip command

It can be used as a package manager pip to install a python module. Lets install a module called pandas using the following command

> pip install pandas

Using a module in Python (Usage)

We use the import syntax to import a module in Python. Here is an example code:


### Read and work with a file named 'words.csv'
> import pandas

> df = pandas.read_csv('words.csv')

> print(df) # This will display first few rows from the words.csv file

Note: Similarly we can install other modules and look into their documentations for usage instructions.

## Comments, Escape sequence & Print in Python

Welcome to Day 5 of 100DaysOfCode. Today we will talk about Comments, Escape Sequences and little bit more about print statement in Python. We will also throw some light on Escape Sequences

### Python Comments

A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

### Single-Line Comments:

To write a comment just add a ‘#’ at the start of the line.

Example 1

> #This is a 'Single-Line Comment'

> print("This is a print statement.")

> Output:

This is a print statement.
Example 2
> print("Hello World !!!") #Printing Hello World
Output:

Hello World !!!
Example 3:
print("Python Program")
#print("Python Program")
Output:
Python Program
Multi-Line Comments:
To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

Example 1: The use of ‘#’.

#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.


> p = 7

> if (p > 5):

>     print("p is greater than 5.")

> else:
>     print("p is not greater than 5.")
 
Output:

p is greater than 5.


Example 2: The use of multiline string.

"""This is an if-else statement.

It will execute a block of code if a specified condition is true.

If the condition is false then it will execute another block of code."""

p = 7

if (p > 5):

    print("p is greater than 5.")

else:

    print("p is not greater than 5.")

Output

p is greater than 5.

Escape Sequence Characters

To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash \ followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

print("This doesnt "execute")

print("This will \" execute")

More on Print statement

The syntax of a print statement looks something like this:

print(object(s), sep=separator, end=end, file=file, flush=flush)

Other Parameters of Print Statement

1. object(s): Any object, and as many as you like. Will be converted to string before printed
2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
3. end='end': Specify what to print at the end. Default is '\n' (line feed)
4. file: An object with a write method. 

Default is sys.stdout


## Variables and Data Types

What is a variable?

> Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as 

writing:

'''
a = 1
b = True
c = "Monu"
d = None
'''

These are four variables of different data types.

What is a Data Type?

Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:

a = 1

print(type(a))

b = "1"

print(type(b))

By default, python provides the following built-in data types:

1. Numeric data: int, float, complex

int: 3, -8, 0

float: 7.349, -9.0, 0.0000001

complex: 6 + 2i

2. Text data: str

str: "Hello World!!!", "Python Programming"

3. Boolean data:

Boolean data consists of values True or False.

4. Sequenced data: list, tuple

list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]

print(list1)

Output:
[8, 2.3, [-4, 5], ['apple', 'banana']]

Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

Example:

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))

print(tuple1)

Output:

(('parrot', 'sparrow'), ('Lion', 'Tiger'))

5. Mapped data: dict

dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

Example:

dict1 = {"name":"Sakshi", "age":20, "canVote":True}

print(dict1)

Output:

{'name': 'Sakshi', 'age': 20, 'canVote': True}


## Operators

Python has different types of operators for different operations. To create a calculator we require arithmetic operators.

Arithmetic operators

Operator	Operator Name	Example

+	           Addition	       15+7
-	           Subtraction	   15-7
*	           Multiplication  5*7
**	           Exponential	   5**3
/	           Division	       5/3
%	           Modulus	       15%7
//	           Floor Division  15//7

> Exercise

n = 15

m = 7

ans1 = n+m

print("Addition of",n,"and",m,"is", ans1)

ans2 = n-m

print("Subtraction of",n,"and",m,"is", ans2)

ans3 = n*m

print("Multiplication of",n,"and",m,"is", ans3)

ans4 = n/m

print("Division of",n,"and",m,"is", ans4)

ans5 = n%m

print("Modulus of",n,"and",m,"is", ans5)

ans6 = n//m

print("Floor Division of",n,"and",m,"is", ans6)

Explaination

Here 'n' and 'm' are two variables in which the integer value is being stored. Variables 'ans1' , 'ans2' ,'ans3', 'ans4','ans5' and 'ans6' contains the outputs corresponding to addition, subtraction,multiplication, division, modulus and floor division respectively.


## TypeCasting

Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users. In this article, we will see the various technique for typecasting.

There can be two types of Type Casting in Python –

1. Implicit Type Casting: Python converts data type into another data type automatically. In this process, users don’t have to involve in this process. 

2. Explicit Type Casting: Python need user involvement to convert the variable data type into certain data type in order to the operation required.

Mainly in type casting can be done with these data type function:

> Int() : Int() function take float or string as an argument and return int type object.
> float() : float() function take int or string as an argument and return float type object.
> str() : str() function take float or int as an argument and return string type object.


## Taking Input from the users 

This function first takes the input from the user and converts it into a string. The type of the returned object always will be <type ‘str’>. It does not evaluate the expression it just returns the complete statement as String. For example, Python provides a built-in function called input which takes the input from the user. When the input function is called it stops the program and waits for the user’s input. When the user presses enter, the program resumes and returns what the user typed. 

Syntax: 

a = input("Enter the value )  

NOTE: WHEN EVER WE PASS THE ANY NUMERIACL VALUE USING INPUT FUNTION IT WILL ONLY CONSIDER IT AS CHARACTER I.E. STRING.

To convert this we will be using TYPECASTING INSIDE THIS FUNCTION.

## String 

A string is a data structure in Python that represents a sequence of characters. It is an immutable data type, meaning that once you have created a string, you cannot change it. Strings are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.

>>  Example: "Mukesh Kumar Sharma"

Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

### Accessing characters in Python String

In Python, individual characters of a String can be accessed by using the method of Indexing. Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 

### Reversing a Python String

With Accessing Characters from a string, we can also reverse them. We can Reverse a string by writing [::-1] and the string will be reversed.

### String Slicing

To access a range of characters in the String, the method of slicing is used. Slicing in a String is done by using a Slicing operator (colon). 

### Deleting/Updating from a String

In Python, the Updation or deletion of characters from a String is not allowed. This will cause an error because item assignment or item deletion from a String is not supported. Although deletion of the entire String is possible with the use of a built-in del keyword. This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned. Only new strings can be reassigned to the same name. 

### Deleting Entire String:

Deletion of the entire string is possible with the use of del keyword. Further, if we try to print the string, this will produce an error because String is deleted and is unavailable to be printed.  

### Escape Sequencing in Python
While printing Strings with single and double quotes in it causes SyntaxError because String already contains Single and Double Quotes and hence cannot be printed with the use of either of these. Hence, to print such a String either Triple Quotes are used or Escape sequences are used to print such Strings. 

Escape sequences start with a backslash and can be interpreted differently. If single quotes are used to represent a string, then all the single quotes present in the string must be escaped and same is done for Double Quotes. 

### Formatting of Strings
Strings in Python can be formatted with the use of format() method which is a very versatile and powerful tool for formatting Strings. Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.

### String methods 

Method	Description
1. capitalize()-->  Converts the first character to upper case
2. casefold()--> Converts string into lower case
3. center()--> Returns a centered string
4. count()--> Returns the number of times a specified value occurs in a string
5. encode()-->	Returns an encoded version of the string
6. endswith()--> Returns true if the string ends with the specified value
7. expandtabs()-->	Sets the tab size of the string
8. find() -->	Searches the string for a specified value and returns the position of where it was found
9. format()-->	Formats specified values in a string
10. format_map()-->	Formats specified values in a string
11. index()-->	Searches the string for a specified value and returns the position of where it was found
12. isalnum()-->	Returns True if all characters in the string are alphanumeric
13. isalpha()-->	Returns True if all characters in the string are in the alphabet
14. isascii()-->	Returns True if all characters in the string are ascii characters
15. isdecimal()-->	Returns True if all characters in the string are decimals
16. isdigit()-->	Returns True if all characters in the string are digits
17. isidentifier()-->	Returns True if the string is an identifier
18. islower()-->	Returns True if all characters in the string are lower case
19. isnumeric()-->	Returns True if all characters in the string are numeric
20. isprintable()-->	Returns True if all characters in the string are printable
21. isspace()-->	Returns True if all characters in the string are whitespaces
22. istitle()-->	Returns True if the string follows the rules of a title
23. isupper()-->	Returns True if all characters in the string are upper case
24. join()-->	Converts the elements of an iterable into a string
25. ljust()-->	Returns a left justified version of the string
26. lower()-->	Converts a string into lower case
27. lstrip()-->	Returns a left trim version of the string
28. maketrans()-->	Returns a translation table to be used in translations
29. partition()-->	Returns a tuple where the string is parted into three parts
30. replace()-->	Returns a string where a specified value is replaced with a specified value
31. rfind()-->	Searches the string for a specified value and returns the last position of where it was found
32. rindex()-->	Searches the string for a specified value and returns the last position of where it was found
33. rjust()-->	Returns a right justified version of the string
34. rpartition()-->	Returns a tuple where the string is parted into three parts
35. rsplit()-->	Splits the string at the specified separator, and returns a list
36. rstrip()-->	Returns a right trim version of the string
37. split()-->	Splits the string at the specified separator, and returns a list
38. splitlines()-->	Splits the string at line breaks and returns a list
39. startswith()-->	Returns true if the string starts with the specified value
40. strip()-->	Returns a trimmed version of the string
41. swapcase()-->	Swaps cases, lower case becomes upper case and vice versa
42. title()-->	Converts the first character of each word to upper case
43. translate()-->	Returns a translated string
44. upper()-->	Converts a string into upper case
45. zfill()-->	Fills the string with a specified number of 0 values at the beginning

## If else statements 

Python supports the usual logical conditions from mathematics:

1. Equals: a == b
2. Not Equals: a != b
3. Less than: a < b
4. Less than or equal to: a <= b
5. Greater than: a > b
6. Greater than or equal to: a >= b


These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

> Example 
> a = 33
> b = 200
> if b > a:
  > print("b is greater than a")

### Indentation

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

### Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

> Example 

> a = 33
> b = 33
> if b > a:
  > print("b is greater than a")
> elif a == b:
  > print("a and b are equal")

## Else
The else keyword catches anything which isn't caught by the preceding conditions.

> Example 

> a = 200
> b = 33
> if b > a:
  > print("b is greater than a")
> elif a == b:
  > print("a and b are equal")
> else:
  > print("a is greater than b")


### Nested If
You can have if statements inside if statements, this is called nested if statements.

> Example
> x = 41

> if x > 10:
  > print("Above ten,")
  > if x > 20:
    > print("and also above 20!")
  > else:
>      print("but not above 20.")



## Match Case Statements

To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements. If this is your first language, dont worry as I will tell you everything you need to know about match case statements in this video!

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case
The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

Syntax:
match variable_name:

            case ‘pattern1’ : //statement1

            case ‘pattern2’ : //statement2

            …            

            case ‘pattern n’ : //statement n

Example:

x = 4
#### x is the variable to match

match x:

    # if x is 0

    case 0:

        print("x is zero")

    # case with if-condition

    case 4 if x % 2 == 0:

        print("x % 2 == 0 and case is 4")

    # Empty case with if-condition

    case _ if x < 10:

        print("x is < 10")

    # default case(will only be matched if the above cases were not matched)

    # so it is basically just an else:

    case _:

        print(x)


## Loop

Python programming language provides the following types of loops to handle looping requirements. Python provides three ways for executing the loops. While all the ways provide similar basic functionality, they differ in their syntax and condition-checking time.

While Loop in Python
In python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.

> Syntax:

> while expression:
  >  statement(s)

All the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code. Python uses indentation as its method of grouping statements. 

Using else statement with While Loop in Python
The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won’t be executed. 

Syntax of While Loop with else statement:

while condition:

     # execute these statements

else:

     # execute these statements

### Infinite While Loop in Python

If we want a block of code to execute infinite number of time, we can use the while loop in Python to do so.

Note: It is suggested not to use this type of loop as it is a never-ending infinite loop where the condition is always true and you have to forcefully terminate the compiler.

### For Loop 

For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is “for in” loop which is similar to for each loop in other languages. Let us learn how to use for in loop for sequential traversals.

Syntax:

> for iterator_var in sequence:
  >   statements(s)

It can be used to iterate over a range and iterators.



## Nested Loops

Python programming language allows to use one loop inside another loop. Following section shows few examples to illustrate the concept. 

Syntax:

for iterator_var in sequence:

   for iterator_var in sequence:

       statements(s)

   statements(s)

The syntax for a nested while loop statement in the Python programming language is as follows: 


while expression:

   while expression: 

       statement(s)

   statement(s)

A final note on loop nesting is that we can put any type of loop inside of any other type of loop. For example, a for loop can be inside a while loop or vice versa.

### Loop Control Statements

Loop control statements change execution from their normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements. 

### Continue Statement
the continue statement in Python returns the control to the beginning of the loop.

### Break Statement
The break statement in Python brings control out of the loop.

### Pass Statement

We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.

How for loop in Python works internally?

Before proceeding to this section, you should have a prior understanding of Python Iterators.

Firstly, lets see how a simple for loop looks like.

Here we can see the for loops iterates over iterable object fruit which is a list. Lists, sets, dictionaries are few iterable objects while an integer object is not an iterable object. For loops can iterate over any of these iterable objects.

Now with the help of the above example, let’s dive deep and see what happens internally here.

1. Make the list (iterable) an iterable object with help of the iter() function.
2. Run an infinite while loop and break only if the StopIteration is raised.
3. In the try block, we fetch the next element of fruits with the next() function.
4. After fetching the element we did the operation to be performed with the element. (i.e print(fruit))



### break statement

The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

### Continue Statement

The continue statement skips the rest of the loop statements and causes the next iteration to occur.

## Function 

Python Functions is a block of statements that return the specific task.

The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again. Some Benefits of Using Functions

1. Increase Code Readability 
2. Increase Code Reusable

### Types of functions:

1. Built-in library function: These are Standard functions in Python that are available to use.
2. User-defined function: We can create our own functions based on our requirements.

### Types of Python Function Arguments

Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following 4 types of function arguments.

0. Default argument
1. Keyword arguments (named arguments)
2. Positional arguments
3. Arbitrary arguments (variable-length arguments *args and **kwargs)

### Default Arguments

A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. The following example illustrates Default arguments.

### Keyword Arguments

The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.

### Positional Arguments

We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age. By changing the position, or if you forget the order of the positions, the values can be used in the wrong places, as shown in the Case-2 example below, where 27 is assigned to the name and Suraj is assigned to the age.

### Arbitrary Keyword  Arguments
In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

> *args in Python (Non-Keyword Arguments)
> **kwargs in Python (Keyword Arguments)

### Docstring

The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

The below syntax can be used to print out the docstring of a function:

> Syntax: print(function_name.__doc__)

### Python Function within Functions

A function that is defined inside another function is known as the inner function or nested function. Nested functions are able to access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function.

### Anonymous functions in Python Function

In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions. Please see this for details.

Return statement in Python function
The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller. The syntax for the return statement is:

> return [expression_list]

The return statement can consist of a variable, an expression, or a constant which is returned at the end of the function execution. If none of the above is present with the return statement a None object is returned.

### Pass by Reference or pass by value

One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.


## List 
In Python, lists are used to store multiple data at once. For example,

Suppose we need to record the ages of 5 students. Instead of creating 5 separate variables, we can simply create a list:

* A list is created in Python by placing items inside [], separated by commas. Here, we have created a list named numbers with 3 integer items. A list can have any number of items and they may be of different types (integer, float, string, etc.)

### Access Python List Elements
In Python, each item in a list is associated with a number. The number is known as a list index.We can access elements of an array using the index number (0, 1, 2 …). The list index always starts with 0. Hence, the first element of a list is present at index 0, not 1.

### Negative Indexing
Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

### Slicing
In Python it is possible to access a section of items from the list using the slicing operator :, not just a single item.

### Methods in shorts 

1. append()	--> add an item to the end of the list
2. extend()	--> add items of lists and other iterables to the end of the list
3. insert()	--> inserts an item at the specified index
4. remove()	--> removes item present at the given index
5. pop()	--> returns and removes item present at the given index
6. clear()	--> removes all items from the list
7. index()	--> returns the index of the first matched item
8. count()	--> returns the count of the specified item in the list
9. sort()	--> sort the list in ascending/descending order
10. reverse()	--> reverses the item of the list
11. copy()	--> returns the shallow copy of the list


## Tuple 
A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

### Creating a Tuple
A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

### Create a Python Tuple With one Element

In Python, creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.

We will need a trailing comma to indicate that it is a tuple,
> var1 = ("Hello") # string
> var2 = ("Hello",) # tuple

### Access Python Tuple Elements

Like a list, each element of a tuple is represented by index numbers (0, 1, ...) where the first element is at index 0.

We use the index number to access tuple elements. For example,

1. Indexing --> We can use the index operator [] to access an item in a tuple, where the index starts from 0.

2. Negative Indexing --> Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

3. Slicing --> We can access a range of items in a tuple by using the slicing operator colon :.

### Advantages of Tuple over List in Python
Since tuples are quite similar to lists, both of them are used in similar situations.

However, there are certain advantages of implementing a tuple over a list:

* We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
* Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
* Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
* If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

## Recursion

Recursion is the process of defining something in terms of itself.

A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

The following image shows the working of a recursive function called recurse.

Following is an example of a recursive function to find the factorial of an integer.

Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.

Our recursion ends when the number reduces to 1. This is called the base condition.

Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.

The Python interpreter limits the depths of recursion to help avoid infinite recursions, resulting in stack overflows.

By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError. Let's look at one such condition.


### Advantages of Recursion
* Recursive functions make the code look clean and elegant.
* A complex task can be broken down into simpler sub-problems using recursion.
* Sequence generation is easier with recursion than using some nested iteration.
### Disadvantages of Recursion
* Sometimes the logic behind recursion is hard to follow through.
* Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
* Recursive functions are hard to debug.

## Set 

A set is a collection of unique data. That is, elements of a set cannot be duplicate. For example,

Suppose we want to store information about student IDs. Since student IDs cannot be duplicate, we can use a set.

### Create a Set in Python
In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.

A set can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

### Create an Empty Set in Python
Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.

To make a set without any elements, we use the set() function without any argument. 

### Duplicate Items in a Set

Let's see what will happen if we try to include duplicate items in a set.

### Add Items to a Set in Python
In Python, we use the add() method to add an item to a set. 

### Update Python Set
The update() method is used to update the set with items other collection types (lists, tuples, sets, etc). 

### Remove an Element from a Set
We use the discard() method to remove the specified element from a set.

Built-in Functions with Set

Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. are commonly used with sets to perform different tasks.

Function	Description
1. all()	--> Returns True if all elements of the set are true (or if the set is empty).
any()	Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
2. len() --> 	Returns the length (the number of items) in the set.
3. max() --> 	Returns the largest item in the set.
4. min()	--> Returns the smallest item in the set.
5. sorted() --> 	Returns a new sorted list from elements in the set(does not sort the set itself).
6. sum() -->	Returns the sum of all elements in the set.


### Python Set Operations

Python Set provides different built-in methods to perform mathematical set operations like union, intersection, subtraction, and symmetric difference.

* Union of Two Sets --> The union of two sets A and B include all the elements of set A and B.
* Set Intersection --> The intersection of two sets A and B include the common elements between set A and B.
* Difference between Two Sets --> The difference between two sets A and B include elements of set A that are not present on set B.
* Set Symmetric Difference --> The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
* Check if two sets are equal --> We can use the == operator to check whether two sets are equal or not.

### Methods 

Other Python Set Methods
There are many set methods, some of which we have already used above. Here is a list of all the methods that are available with the set objects:

Method	Description
1. add()	Adds an element to the set
2. clear()	Removes all elements from the set
3. copy()	Returns a copy of the set
4. difference()	Returns the difference of two or more sets as a new set
5. difference_update()	Removes all elements of another set from this set
6. discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
7. intersection()	Returns the intersection of two sets as a new set
8. intersection_update()	Updates the set with the intersection of itself and another
9. isdisjoint()	Returns True if two sets have a null intersection
10. issubset()	Returns True if another set contains this set
11. issuperset()	Returns True if this set contains another set
12. pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
13. remove()	Removes an element from the set. If the element is not a member, raises a KeyError
14. symmetric_difference()	Returns the symmetric difference of two sets as a new set
15. symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
16. union()	Returns the union of sets in a new set
17. update()	Updates the set with the union of itself and others

## Dictionary

Python dictionary is an ordered collection (starting from Python 3.7) of items. It stores elements in key/value pairs. Here, keys are unique identifiers that are associated with each value.

Let's see an example,

If we want to store information about countries and their capitals, we can create a dictionary with country names as keys and capitals as values.

Keys	Values

Nepal	Kathmandu

Italy	Rome

England	London

### Methods 

1. all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
2. any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
3. len()	Return the length (the number of items) in the dictionary.
4. sorted()	Return a new sorted list of keys in the dictionary.
5. clear()	Removes all items from the dictionary.
6. keys()	Returns a new object of the dictionary's keys.
7. values()	Returns a new object of the dictionary's values

### Dictionary Membership Test
We can test if a key is in a dictionary or not using the keyword in. Notice that the membership test is only for the keys and not for the values.
> **check code for all examples**


## Exception Handling
An exception is an unexpected event that occurs during program execution. For example,
> divide_by_zero = 7 / 0
The above code causes an exception as it is not possible to divide a number by 0.

Logical Errors (Exceptions)
Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.

For instance, they occur when we

* try to open a file(for reading) that does not exist (FileNotFoundError)
* try to divide a number by zero (ZeroDivisionError)
* try to import a module that does not exist (ImportError) and so on.

Whenever these types of runtime errors occur, Python creates an exception object.

If not handled properly, it prints a traceback to that error along with some details about why that error occurred.

### Python Built-in Exceptions

Illegal operations can raise exceptions. There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.

We can view all the built-in exceptions using the built-in local() function as follows:

> print(dir(locals()['__builtins__']))

### Error and Exception

Errors represent conditions such as compilation error, syntax error, error in the logical part of the code, library incompatibility, infinite recursion, etc.

Errors are usually beyond the control of the programmer and we should not try to handle errors.

## Exceptions can be caught and handled by the program.

The try...except block is used to handle exceptions in Python. Here's the syntax of try...except block:

"""try:
    # code that may cause exception
except:
    # code to run when exception occurs

"""

Here, we have placed the code that might generate an exception inside the try block. Every try block is followed by an except block.

When an exception occurs, it is caught by the except block. The except block cannot be used without the try block.

### Catching Specific Exceptions in Python

For each try block, there can be zero or more except blocks. Multiple except blocks allow us to handle each exception differently.

The argument type of each except block indicates the type of exception that can be handled by it. 

### try with else clause

In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.

For these cases, you can use the optional else keyword with the try statement.

### try...finally
In Python, the finally block is always executed no matter whether there is an exception or not.

The finally block is optional. And, for each try block, there can be only one finally block.

## Custon exception

Raising Custom errors
In python, we can raise custom errors by using the raise keyword.

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:

class CustomError(Exception):
  #### code ...
  pass

try:
  #### code ...

except CustomError:
  #### code...

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.

## How importing in python works

Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

> import math

Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the sqrt function from the math module, you would write:

> import math

> result = math.sqrt(9)
> print(result)  # Output: 3.0

> from keyword

You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, you would write:

> from math import sqrt

> result = sqrt(9)
> print(result)  # Output: 3.0

You can also import multiple functions or variables at once by separating them with a comma:

> from math import sqrt, pi

> result = sqrt(9)
> print(result)  # Output: 3.0

> print(pi)  # Output: 3.141592653589793

importing everything

It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.

> from math import *

> result = sqrt(9)
> print(result)  # Output: 3.0

> print(pi)  # Output: 3.141592653589793


Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.

> The "as" keyword
> import math as m

> result = m.sqrt(9)
> print(result)  # Output: 3.0

> print(m.pi)  # Output: 3.141592653589793

The dir function

Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.

> import math

> print(dir(math))

This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.

In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current script. You can import the entire module, specific functions or variables, or use the * wildcard to import everything. You can also use the as keyword to rename a module, and the dir function to view the contents of a module.

## OS module 

The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.

### Handling the Current Working Directory
Consider Current Working Directory(CWD) as a folder, where the Python is operating. Whenever the files are called only by their name, Python assumes that it starts in the CWD which means that name-only reference will be successful only if the file is in the Python’s CWD.
Note: The folder where the Python script is running is known as the Current Directory. This is not the path where the Python script is located.

### Changing the Current working directory

To change the current working directory(CWD) os.chdir() method is used. This method changes the CWD to a specified path. It only takes a single argument as a new directory path.
 
Note: The current working directory is the folder in which the Python script is operating.

### Creating a Directory
There are different methods available in the OS module for creating a directory. These are –

* os.mkdir()
* os.makedirs()
* Using os.mkdir()

os.mkdir() method in Python is used to create a directory named path with the specified numeric mode. This method raises FileExistsError if the directory to be created already exists.

### Using os.makedirs()
os.makedirs() method in Python is used to create a directory recursively. That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.

### Listing out Files and Directories with Python
os.listdir() method in Python is used to get the list of all files and directories in the specified directory. If we don’t specify any directory, then the list of files and directories in the current working directory will be returned.

### Deleting Directory or Files using Python
OS module proves different methods for removing directories and files in Python. These are – 

1. Using os.remove()
2. Using os.rmdir()
3. Using os.remove()

os.remove() method in Python is used to remove or delete a file path. This method can not remove or delete a directory. If the specified path is a directory then OSError will be raised by the method.

### Using os.rmdir()
os.rmdir() method in Python is used to remove or delete an empty directory. OSError will be raised if the specified path is not an empty directory.

### Commonly Used Functions
1. os.name: This function gives the name of the operating system dependent module imported. The following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’.

2. os.error: All functions in this module raise OSError in the case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system. os.error is an alias for built-in OSError exception. 

3. os.popen(): This method opens a pipe to or from command. The return value can be read or written depending on whether the mode is ‘r’ or ‘w’. 
Syntax: 

 > os.popen(command[, mode[, bufsize]])

4. os.close(): Close file descriptor fd. A file opened using open(), can be closed by close()only. But file opened through os.popen(), can be closed with close() or os.close(). If we try closing a file opened with open(), using os.close(), Python would throw TypeError. 

5. os.rename(): A file old.txt can be renamed to new.txt, using the function os.rename(). The name of the file changes only if, the file exists and the user has sufficient privilege permission to change the file.

6. os.remove(): Using the Os module we can remove a file in our system using the remove() method. To remove a file we need to pass the name of the file as a parameter. 

7. os.path.exists(): This method will check whether a file exists or not by passing the name of the file as a parameter. OS module has a sub-module named PATH by using which we can perform many more functions. 

8. os.path.getsize(): In this method, python will give us the size of the file in bytes. To use this method we need to pass the name of the file as a parameter.
 
for more: https://docs.python.org/3/library/os.html

## Local variable and global variable 

* Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function. 

### The global Keyword

We only need to use the global keyword in a function if we want to do assignments or change the global variable. global is not needed for printing and accessing. Python “assumes” that we want a local variable due to the assignment to s inside of f(), so the first statement throws the error message. Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. To tell Python, that we want to use the global variable, we have to use the keyword “global”

> These are those which are defined outside any function and which are accessible throughout the program, i.e., inside and outside of every function. Let’s see how to create a Python global variable.

* Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function. Let’s see how to create a local variable.

"""
Why do we use Local and Global variables in Python?
Now, what if there is a Python variable with the same name initialized inside a function as well as globally? Now the question arises, will the local variable will have some effect on the global variable or vice versa, and what will happen if we change the value of a variable inside of the function f()
"""

## OOPs-> Object Oriented Programming

Object-Oriented Programming, also known as OOPs concepts in python, is what lets us develop applications using an Object-Oriented approach. It does so by clubbing together similar or related behaviors and properties and converting them into objects.

Developers often choose to use OOP concepts in Python programs because it makes code more reusable and easier to work with larger programs. OOP programs prevent you from repeating code because a class can be defined once and reused many times.

Object-Oriented Programming(OOP), a programming paradigm, is all about creating “objects.” An object is a group of interrelated variables and functions. These variables are often referred to as properties of the object, and functions are referred to as the behavior of the objects. These objects provide a better and clear structure for the program.

For example, a car can be an object. If we consider the car as an object, its properties would be its color, model, price, brand, etc. And its behavior/function would be acceleration, slowing down, and gear change.

Another example – If we consider a dog as an object then its properties would be its color, breed, name, weight, etc., and its behavior/function would be walking, barking, playing, etc.

Object-Oriented Programming is famous because it implements real-world entities like objects, hiding, inheritance, etc, in programming. It makes visualization easier because it is close to real-world scenarios.

### Difference between OOPs and POP (Procedural oriented programming)

* One way to think about POP is the same way you make lemonade, for example. The procedure of making lemonade involves- first taking water according to the need, then adding sugar to the water, then adding lemon juice to the mixture, and finally mixing the whole solution. And your lemonade is ready to serve. Similarly, POP requires a certain procedure of steps. A procedural program consists of functions. This means that in the POP approach, the program is divided into functions that are specific to different tasks. These functions are arranged in a specific sequence, and the control of the program flows sequentially.

* On the other hand, an OOP program consists of objects. The object-Oriented approach divides the program into objects. And these objects are the entities that bundle up the properties and the behavior of real-world objects.
POP is suitable for small tasks only. Because as the program’s length increases, the code’s complexity also increases. And it ends up becoming a web of functions. Also, it becomes hard to debug. OOP solves this problem with the help of a clearer and less complex structure. It allows code re-usability in the form of inheritance.

* Another important thing is that in procedure-oriented programming, all the functions have access to all the data, which implies a lack of security. Suppose you want to secure the credentials or any other critical information from the world. Then the procedural approach fails to provide you with that security. For this OOP helps you with one of its amazing functionality known as Encapsulation, which allows us to hide data. Don’t worry I’ll cover this in detail in the latter part of this article along with other concepts of Object-Oriented Programming. For now, just understand that OOP enables security and POP does not.

What Is a Class?
A straightforward answer to this question is- A class is a collection of objects.  Unlike primitive data structures, classes are data structures that the user defines. They make the code more manageable.

Let’s see how to define a class below-

class class_name:
    
    class body

We define a new class with the keyword “class” following the class_name and colon. And we consider everything you write under this after using indentation as its body. To make this more understandable, let’s see an example.

### Objects and Object Instantiation

When we define a class, only the description or a blueprint of the object is created. There is no memory allocation until we create its object. The objector instance contains real data or information.

Instantiation is nothing but creating a new object/instance of a class. Let’s create the object of the above class we defined-

obj1 = Car()
And it’s done! Note that you can change the object name according to your choice.

Class Constructor
Until now, we have had an empty class Car, time to fill up our class with the properties of the car.  The job of the class constructor is to assign the values to the data members of the class when an object of the class is created.

There can be various properties of a car, such as its name, color, model, brand name, engine power, weight, price, etc. We’ll choose only a few for understanding purposes.

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

So, the properties of the car or any other object must be inside a method that we call __init__( ). This __init__() method is also known as the constructor method. We call a constructor method whenever an object of the class is constructed.

The two statements inside the constructor method are –

1. self.name = name
2. self.color = color:

This will create new attributes, namely name and color, and then assign the value of the respective parameters to them. The “self” keyword represents the instance of the class. By using the “self” keyword, we can access the attributes and methods of the class. It is useful in method definitions and in variable initialization. The “self” is explicitly used every time we define a method.

Note: You can also create attributes outside of this __init__() method. But those attributes will be universal to the whole class, and you will have to assign a value to them.

Suppose all the cars in your showroom are Sedan, and instead of specifying it again and again, you can fix the value of car_type as Sedan by creating an attribute outside the __init__().

class Car:
    
    car_type = "Sedan"                 #class attribute
    
    def __init__(self, name, color):
        
        self.name = name               #instance attribute   
        
        self.color = color             #instance attribute


Here, Instance attributes refer to the attributes inside the constructor method, i.e., self.name and self.color. And Class attributes refer to the attributes outside the constructor method, i.e., car_type.

Class Methods

So far, we’ve added the properties of the car. Now it’s time to add some behavior. Methods are the functions we use to describe the behavior of objects. They are also defined inside a class.

The methods defined inside a class other than the constructor method are known as the instance methods. Furthermore, we have two instance methods here – description() and max_speed(). Let’s talk about them individually:

* description()- This method returns a string with the description of the car, such as the name and its mileage. This method has no additional parameter. This method uses instance attributes.

* max_speed()- This method has one additional parameter and returns a string displaying the car’s name and speed.
Notice that the additional parameter speed is not using the “self” keyword. Since speed is not an instance variable, we don’t use the self keyword as its prefix. Let’s create an object for the class described above.

obj2 = Car("Honda City",24.1)

print(obj2.description())

print(obj2.max_speed(150))

Note: Three important things to remember are-

1. You can create any number of objects in a class.
2. If the method requires n parameters and you do not pass the same number of arguments, then an error will occur.
3. The order of the arguments matters.

### Inheritance in Python Class
Inheritance is the procedure in which one class inherits the attributes and methods of another class.  The class whose properties and methods are inherited is known as the Parent class. And the class that inherits the properties from the parent class is the Child class.

The interesting thing is, along with the inherited properties and methods, a child class can have its own properties and methods.

Syntax

class parent_class:
  
  body of parent class

class child_class( parent_class):
  
  body of child class

### Encapsulation

Encapsulation, as I mentioned in the initial part of the article, is a way to ensure security. Basically, it hides the data from the access of outsiders. Such as, if an organization wants to protect an object/information from unwanted access by clients or any unauthorized person, then encapsulation is the way to ensure this.

You can declare the methods or the attributes protected by using a single underscore ( ) before their names, such as _self.name or def _method( ); Both of these lines tell that the attribute and method are protected and should not be used outside the access of the class and sub-classes but can be accessed by class methods and objects.

Though Python uses ‘ _ ‘ just as a coding convention, it tells that you should use these attributes/methods within the scope of the class. But you can still access the variables and methods which are defined as protected, as usual.

Now to actually prevent the access of attributes/methods from outside the scope of a class, you can use “private members“. In order to declare the attributes/method as private members, use double underscore ( ) in the prefix. Such as – self.name or def __method(); Both of these lines tell that the attribute and method are private and access is not possible from outside the class.

### Introduction
Object-Oriented Programming, also known as OOPs concepts in python, is what lets us develop applications using an Object-Oriented approach. It does so by clubbing together similar or related behaviors and properties and converting them into objects. In this article, I will explain the basic concepts of Object-Oriented Programming in Python programming, oop fundamentals, and features of oops. You must know Python programming before you continue.

Developers often choose to use OOP concepts in Python programs because it makes code more reusable and easier to work with larger programs. OOP programs prevent you from repeating code because a class can be defined once and reused many times.

Beginners can learn Python using the free course on Introduction to Python.
Learning Objectives

Understanding the Object Oriented Programming.
Learning and implementing different OOP concepts in python.
Table of Contents
The History of Object-Oriented Programming
What Is Object-Oriented Programming?
Object-Oriented Programming (OOP) vs Procedure Oriented Programming (POP)
Major OOPs Concepts in Python
Conclusion
The History of Object-Oriented Programming
While learning Object-Oriented Programming (oops concepts), I decided to dive into its history to fully know what is oops concept and it turned out to be fascinating. The term “Object-Oriented Programming” (OOP), also known as oops concepts in python, was coined by Alan Kay around 1966 while he was at grad school. The language called Simula was the first programming language with the features of Object-oriented programming. It was developed in 1967 for making simulation programs, in which the most important information was called objects.

oops concepts in python

Though OOPs were in the market since the early 1960s it was in the 1990s that OOPs began to grow because of C++. After that, this technique was adopted by various programmers across various programming languages, including Python. Today its application is in almost every field, such as Real-time systems, machine learning, Artificial intelligence, Data Science, expert systems, Client-server systems, Object-oriented databases, and many more.


Become a Full-Stack Data Scientist
Power Ahead in your AI ML Career | No Pre-requisites Required

What Is Object-Oriented Programming?
Object-Oriented Programming(OOP), a programming paradigm, is all about creating “objects.” An object is a group of interrelated variables and functions. These variables are often referred to as properties of the object, and functions are referred to as the behavior of the objects. These objects provide a better and clear structure for the program.

For example, a car can be an object. If we consider the car as an object, its properties would be its color, model, price, brand, etc. And its behavior/function would be acceleration, slowing down, and gear change.

Another example – If we consider a dog as an object then its properties would be its color, breed, name, weight, etc., and its behavior/function would be walking, barking, playing, etc.

Object-Oriented Programming is famous because it implements real-world entities like objects, hiding, inheritance, etc, in programming. It makes visualization easier because it is close to real-world scenarios.

Object-Oriented Programming (OOP) vs Procedure Oriented Programming (POP)
The basic differences between OOP and POP are the following:

One way to think about POP is the same way you make lemonade, for example. The procedure of making lemonade involves- first taking water according to the need, then adding sugar to the water, then adding lemon juice to the mixture, and finally mixing the whole solution. And your lemonade is ready to serve. Similarly, POP requires a certain procedure of steps. A procedural program consists of functions. This means that in the POP approach, the program is divided into functions that are specific to different tasks. These functions are arranged in a specific sequence, and the control of the program flows sequentially.
On the other hand, an OOP program consists of objects. The object-Oriented approach divides the program into objects. And these objects are the entities that bundle up the properties and the behavior of real-world objects.
POP is suitable for small tasks only. Because as the program’s length increases, the code’s complexity also increases. And it ends up becoming a web of functions. Also, it becomes hard to debug. OOP solves this problem with the help of a clearer and less complex structure. It allows code re-usability in the form of inheritance.
Another important thing is that in procedure-oriented programming, all the functions have access to all the data, which implies a lack of security. Suppose you want to secure the credentials or any other critical information from the world. Then the procedural approach fails to provide you with that security. For this OOP helps you with one of its amazing functionality known as Encapsulation, which allows us to hide data. Don’t worry I’ll cover this in detail in the latter part of this article along with other concepts of Object-Oriented Programming. For now, just understand that OOP enables security and POP does not.
Programming languages like C, Pascal, and BASIC use the procedural approach, whereas  Java, Python, JavaScript, PHP, Scala, and C++ are the main languages that provide the Object-oriented approach.
Major OOPs Concepts in Python
In this section, we will dive deep into the basic concepts of OOP, covering topics such as class, object, method, inheritance, encapsulation, polymorphism, and data abstraction.

What Is a Class?
A straightforward answer to this question is- A class is a collection of objects.  Unlike primitive data structures, classes are data structures that the user defines. They make the code more manageable.

Let’s see how to define a class below-

class class_name:
    class body
We define a new class with the keyword “class” following the class_name and colon. And we consider everything you write under this after using indentation as its body. To make this more understandable, let’s see an example.

Consider the case of a car showroom. You want to store the details of each car. Let’s start by defining a class first-

class Car:
    pass
That’s it!

Note: I’ve used the pass statement in place of its body because the main aim was to show how you can define a class and not what it should contain.

Even the datatypes in Python, like tuples,dictionaries, etc. are classes.

Before going into detail, first, understand objects and instantiation.

Objects and Object Instantiation
When we define a class, only the description or a blueprint of the object is created. There is no memory allocation until we create its object. The objector instance contains real data or information.

Instantiation is nothing but creating a new object/instance of a class. Let’s create the object of the above class we defined-

obj1 = Car()
And it’s done! Note that you can change the object name according to your choice.

Try printing this object-

print(obj1)
oops concepts in python - Object Instantiation

Since our class was empty, it returns the address where the object is stored i.e. 0x7fc5e677b6d8

You also need to understand the class constructor before moving forward.

Class Constructor
Until now, we have had an empty class Car, time to fill up our class with the properties of the car.  The job of the class constructor is to assign the values to the data members of the class when an object of the class is created.

There can be various properties of a car, such as its name, color, model, brand name, engine power, weight, price, etc. We’ll choose only a few for understanding purposes.

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
So, the properties of the car or any other object must be inside a method that we call __init__( ). This __init__() method is also known as the constructor method. We call a constructor method whenever an object of the class is constructed.

Now let’s talk about the parameter of the __init__() method. So, the first parameter of this method has to be self. Then only will the rest of the parameters come.

The two statements inside the constructor method are –

self.name = name
self.color = color:
This will create new attributes, namely name and color, and then assign the value of the respective parameters to them. The “self” keyword represents the instance of the class. By using the “self” keyword, we can access the attributes and methods of the class. It is useful in method definitions and in variable initialization. The “self” is explicitly used every time we define a method.

Note: You can also create attributes outside of this __init__() method. But those attributes will be universal to the whole class, and you will have to assign a value to them.

Suppose all the cars in your showroom are Sedan, and instead of specifying it again and again, you can fix the value of car_type as Sedan by creating an attribute outside the __init__().

class Car:
    car_type = "Sedan"                 #class attribute
    def __init__(self, name, color):
        self.name = name               #instance attribute   
        self.color = color             #instance attribute
Here, Instance attributes refer to the attributes inside the constructor method, i.e., self.name and self.color. And Class attributes refer to the attributes outside the constructor method, i.e., car_type.

Class Methods
So far, we’ve added the properties of the car. Now it’s time to add some behavior. Methods are the functions we use to describe the behavior of objects. They are also defined inside a class. Look at the following code-
Python Code:


The methods defined inside a class other than the constructor method are known as the instance methods. Furthermore, we have two instance methods here – description() and max_speed(). Let’s talk about them individually:

description()- This method returns a string with the description of the car, such as the name and its mileage. This method has no additional parameter. This method uses instance attributes.
max_speed()- This method has one additional parameter and returns a string displaying the car’s name and speed.
Notice that the additional parameter speed is not using the “self” keyword. Since speed is not an instance variable, we don’t use the self keyword as its prefix. Let’s create an object for the class described above.

obj2 = Car("Honda City",24.1)
print(obj2.description())
print(obj2.max_speed(150))
oops concepts in python - Max_Speed and Description

What we did was we created an object of class car and passed the required arguments. To access the instance methods, we use object_name.method_name().

The method description() didn’t have any additional parameter, so we did not pass any argument while calling it.

The method max_speed() has one additional parameter, so we passed one argument while calling it.

Note: Three important things to remember are-

You can create any number of objects in a class.
If the method requires n parameters and you do not pass the same number of arguments, then an error will occur.
The order of the arguments matters.
Let’s look at these, one by one:

Creating more than one object of a class
class Car:

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"
Honda = Car("Honda City",21.4)
print(Honda.max_speed(150))

Skoda = Car("Skoda Octavia",13)
print(Skoda.max_speed(210))
oops concepts in python - Creating more than one object

Passing the wrong number of arguments

class Car:

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage
Honda = Car("Honda City")
print(Honda)
Object Oriented Programming - Passing the wrong number of arguments

Since we did not provide the second argument, we got this error.
Order of the arguments

class Car:

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"
Honda = Car(24.1,"Honda City")
print(Honda.description())
oops concepts in python - Argument Order

Messed up! Notice we changed the order of arguments.
There are four fundamental concepts of Object-oriented programming – Inheritance, Encapsulation, Polymorphism, and Data abstraction. It is essential to know about all of these in order to understand OOPs. Till now, we’ve covered the basics of OOPs concepts in python; let’s dive in further.

Inheritance in Python Class
Inheritance is the procedure in which one class inherits the attributes and methods of another class.  The class whose properties and methods are inherited is known as the Parent class. And the class that inherits the properties from the parent class is the Child class.

The interesting thing is, along with the inherited properties and methods, a child class can have its own properties and methods.

How to inherit a parent class? Use the following syntax:

class parent_class:
body of parent class

class child_class( parent_class):
body of child class
Let’s see the implementation:

class Car:          #parent class

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class BMW(Car):     #child class
    pass

class Audi(Car):     #child class
    def audi_desc(self):
        return "This is the description method of class Audi."
obj1 = BMW("BMW 7-series",39.53)
print(obj1.description())

obj2 = Audi("Audi A8 L",14)
print(obj2.description())
print(obj2.audi_desc())
oops concepts in python | Inheritence

We have created two child classes, namely “BMW” and “Audi,” who have inherited the methods and properties of the parent class “Car.”  We have provided no additional features and methods in the class BMW. Whereas one additional method inside the class Audi.

Notice how the instance method description() of the parent class is accessible by the objects of child classes with the help of obj1.description() and obj2.description(). The separate method of class Audi is also accessible using obj2.audi_desc().

Encapsulation
Encapsulation, as I mentioned in the initial part of the article, is a way to ensure security. Basically, it hides the data from the access of outsiders. Such as, if an organization wants to protect an object/information from unwanted access by clients or any unauthorized person, then encapsulation is the way to ensure this.

You can declare the methods or the attributes protected by using a single underscore ( ) before their names, such as _self.name or def _method( ); Both of these lines tell that the attribute and method are protected and should not be used outside the access of the class and sub-classes but can be accessed by class methods and objects.

Though Python uses ‘ _ ‘ just as a coding convention, it tells that you should use these attributes/methods within the scope of the class. But you can still access the variables and methods which are defined as protected, as usual.

Now to actually prevent the access of attributes/methods from outside the scope of a class, you can use “private members“. In order to declare the attributes/method as private members, use double underscore ( ) in the prefix. Such as – self.name or def __method(); Both of these lines tell that the attribute and method are private and access is not possible from outside the class.

class car:

    def __init__(self, name, mileage):
        self._name = name                #protected variable
        self.mileage = mileage 

    def description(self):                
        return f"The {self._name} car gives the mileage of {self.mileage}km/l"
obj = car("BMW 7-series",39.53)

#accessing protected variable via class method 
print(obj.description())

#accessing protected variable directly from outside
print(obj._name)
print(obj.mileage)
Object oriented Programming - Encapsulation

Notice how we accessed the protected variable without any error. It is clear that access to the variable is still public. Let us see how encapsulation works-
class Car:

    def __init__(self, name, mileage):
        self.__name = name              #private variable        
        self.mileage = mileage 

    def description(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage}km/l"
obj = Car("BMW 7-series",39.53)

#accessing private variable via class method 
print(obj.description())

#accessing private variable directly from outside
print(obj.mileage)
print(obj.__name)
Encapsulation

When we tried accessing the private variable using the description() method, we encountered no error. But when we tried accessing the private variable directly outside the class, then Python gave us an error stating: car object has no attribute ‘__name’.

You can still access this attribute directly using its mangled name. Name mangling is a mechanism we use for accessing the class members from outside. The Python interpreter rewrites any identifier with “__var” as “_ClassName__var”. And using this you can access the class member from outside as well.

class Car:

    def __init__(self, name, mileage):
        self.__name = name              #private variable        
        self.mileage = mileage 

    def description(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage}km/l"
obj = Car("BMW 7-series",39.53)

#accessing private variable via class method 
print(obj.description())

#accessing private variable directly from outside
print(obj.mileage)
print(obj._Car__name)      #mangled name
Encapsulation Example | oops concepts in python

Note that the mangling rule’s design mostly avoids accidents. But it is still possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

### Polymorphism

This is a Greek word. If we break the term Polymorphism, we get “poly”-many and “morph”-forms. So Polymorphism means having many forms. In OOP it refers to the functions having the same names but carrying different functionalities.

### Data Abstraction
We use Abstraction for hiding the internal details or implementations of a function and showing its functionalities only. This is similar to the way you know how to drive a car without knowing the background mechanism. Or you know how to turn on or off a light using a switch, but you don’t know what is happening behind the socket.

Any class with at least one abstract function is an abstract class. To create an abstraction class, first, you need to import the ABC class from abc module. This lets you create abstract methods inside it. ABC stands for Abstract Base Class.

### Key Points to Remember:
* Object-Oriented Programming makes the program easy to understand as well as efficient.
* Since the class is sharable, the code can be reused.
* Data is safe and secure with data abstraction.
* Polymorphism allows the same interface for different objects, so programmers can write efficient code.

## Lambda functions

Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 

> Syntax: lambda arguments: expression

* This function can have any number of arguments but only one expression, which is evaluated and returned.
* One is free to use lambda functions wherever function objects are required.
* You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
* It has various uses in particular fields of programming, besides other types of expressions in functions.

## Map(), Reduce(), and Filter()

In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

1. Map(): The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

> map(function, iterable)
The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

2. Filter(): The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

> filter(predicate, iterable)

The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

3. Reduce(): The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

> reduce(function, iterable)

The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

## Method Overloading 

Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

In Python, method overriding is a way to customize the behavior of a class based on its specific needs. For example, consider the following base class:

In this example, the Circle class inherits from the Shape class, and overrides the area method. The new implementation of the area method calculates the area of a circle, based on its radius.

It's important to note that when you override a method, the new implementation must have the same method signature as the original method. This means that the number and type of arguments, as well as the return type, must be the same.

Another way to customize the behavior of a class is to call the base class method from the derived class method. To do this, you can use the super function. The super function allows you to call the base class method from the derived class method, and can be useful when you want to extend the behavior of the base class method, rather than replace it.

## Creating Command Line Utilities in Python
Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In Python, you can create your own command line utilities using the built-in argparse module.
