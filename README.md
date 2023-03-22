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

