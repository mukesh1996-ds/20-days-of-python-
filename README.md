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

>>  Example: "Mukesh Kumar Sharma

Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

### Accessing characters in Python String

In Python, individual characters of a String can be accessed by using the method of Indexing. Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 

<img src="C:\Users\mukeshkr\Desktop\WORK\Coding\Personal Data\20-days-of-python-\images\string indexing example.jpg" width="128"/>

