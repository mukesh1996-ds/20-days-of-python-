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
object(s): Any object, and as many as you like. Will be converted to string before printed
sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
end='end': Specify what to print at the end. Default is '\n' (line feed)
file: An object with a write method. Default is sys.stdout
