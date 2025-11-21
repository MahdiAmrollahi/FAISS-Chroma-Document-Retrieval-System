# Python Programming Concepts: From Basics to Intermediate

## Table of Contents
1. [Introduction to Python](#introduction)
2. [Basic Syntax](#basic-syntax)
3. [Data Types](#data-types)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Data Structures](#data-structures)
7. [Object-Oriented Programming](#oop)
8. [File Handling](#file-handling)
9. [Error Handling](#error-handling)
10. [Modules and Packages](#modules)
11. [List Comprehensions](#list-comprehensions)
12. [Lambda Functions](#lambda)
13. [Decorators](#decorators)
14. [Generators](#generators)

---

## Introduction to Python {#introduction}

Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms including procedural, object-oriented, and functional programming.

### Why Python?
- Easy to learn and read
- Versatile and powerful
- Large standard library
- Active community support
- Cross-platform compatibility

---

## Basic Syntax {#basic-syntax}

### Variables and Assignment

```python
# Variable assignment
name = "Python"
age = 30
price = 19.99
is_active = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Variable naming conventions
user_name = "john"  # snake_case (recommended)
userName = "john"    # camelCase (also valid)
```

### Comments

```python
# This is a single-line comment

"""
This is a multi-line comment
or docstring
"""

def my_function():
    """This is a function docstring."""
    pass
```

### Print Statement

```python
print("Hello, World!")
print("Name:", name, "Age:", age)
print(f"Name: {name}, Age: {age}")  # f-string (Python 3.6+)
print("Name: {}, Age: {}".format(name, age))  # .format() method
```

---

## Data Types {#data-types}

### Numeric Types

```python
# Integers
num1 = 42
num2 = -10
num3 = 0

# Floating Point
float1 = 3.14
float2 = -0.5
float3 = 2.0e3  # Scientific notation: 2000.0

# Complex Numbers
complex_num = 3 + 4j

# Type checking
print(type(num1))      # <class 'int'>
print(type(float1))   # <class 'float'>
print(type(complex_num))  # <class 'complex'>
```

### Strings

```python
# String creation
str1 = "Hello"
str2 = 'World'
str3 = """Multi-line
string"""
str4 = '''Another multi-line
string'''

# String operations
full_name = str1 + " " + str2  # Concatenation
repeated = "Hi" * 3  # "HiHiHi"
length = len(full_name)  # Get length

# String methods
text = "  Python Programming  "
print(text.strip())           # "Python Programming"
print(text.upper())           # "  PYTHON PROGRAMMING  "
print(text.lower())           # "  python programming  "
print(text.replace("Python", "Java"))  # "  Java Programming  "
print(text.split())           # ['Python', 'Programming']
print("Python".startswith("Py"))  # True
print("Python".endswith("on"))    # True

# String indexing and slicing
text = "Python"
print(text[0])        # 'P'
print(text[-1])       # 'n' (last character)
print(text[0:3])      # 'Pyt' (slicing)
print(text[:3])       # 'Pyt' (from start)
print(text[3:])       # 'hon' (to end)
print(text[::-1])     # 'nohtyP' (reverse)
```

### Boolean

```python
# Boolean values
is_true = True
is_false = False

# Boolean operations
result1 = True and False   # False
result2 = True or False    # True
result3 = not True         # False

# Truthy and Falsy values
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("text")) # True
print(bool([]))     # False
print(bool([1, 2])) # True
```

### None Type

```python
value = None
print(value is None)  # True
print(value == None)  # True (but prefer 'is')
```

---

## Control Flow {#control-flow}

### Conditional Statements

```python
# if-else
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
x = 10
if 0 < x < 20:  # Python allows chained comparisons
    print("x is between 0 and 20")
```

### Loops

#### For Loop

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterating over dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")
```

#### While Loop

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

# While with continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # Only odd numbers
```

#### Loop Control Statements

```python
# break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# else with loops (executes if loop completes normally)
for i in range(5):
    print(i)
else:
    print("Loop completed")  # Always executes

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")  # Won't execute if break occurs
```

---

## Functions {#functions}

### Basic Functions

```python
# Function definition
def greet():
    print("Hello, World!")

# Function call
greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}"

print(greet_with_title("Smith"))           # "Hello, Mr. Smith"
print(greet_with_title("Smith", "Dr."))    # "Hello, Dr. Smith"

# Function with keyword arguments
def create_profile(name, age, city):
    return f"{name}, {age}, lives in {city}"

print(create_profile(name="John", age=30, city="NYC"))
print(create_profile(city="LA", name="Jane", age=25))  # Order doesn't matter

# Function with variable arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15

# Function with keyword variable arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="NYC")

# Combining all argument types
def complex_function(required, default="value", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("req", "def", 1, 2, 3, key1="val1", key2="val2")
```

### Lambda Functions

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

### Scope and Global Variables

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)

# Modifying global variable
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

---

## Data Structures {#data-structures}

### Lists

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List operations
fruits.append("orange")        # Add to end
fruits.insert(1, "grape")      # Insert at index
fruits.remove("banana")        # Remove by value
fruits.pop()                   # Remove last item
fruits.pop(0)                  # Remove by index
fruits.sort()                  # Sort in place
fruits.reverse()               # Reverse in place

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3]
print(numbers[:3])     # [0, 1, 2]
print(numbers[3:])     # [3, 4, 5]
print(numbers[::2])    # [0, 2, 4] (step by 2)

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Tuples

```python
# Creating tuples
point = (3, 4)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma

# Tuple unpacking
x, y = point
print(f"x: {x}, y: {y}")

# Tuples are immutable
# point[0] = 5  # This would cause an error

# Tuple operations
print(len(colors))           # 3
print("red" in colors)       # True
print(colors + ("yellow",))  # Concatenation
```

### Dictionaries

```python
# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])        # "John"
print(person.get("age"))     # 30
print(person.get("email", "N/A"))  # "N/A" (default if key doesn't exist)

# Modifying dictionaries
person["email"] = "john@example.com"
person["age"] = 31
person.update({"city": "Boston", "country": "USA"})

# Dictionary methods
print(person.keys())         # dict_keys(['name', 'age', 'city', ...])
print(person.values())       # dict_values(['John', 31, 'Boston', ...])
print(person.items())        # dict_items([('name', 'John'), ...])

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Sets

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4, 5])

# Set operations
fruits.add("orange")
fruits.remove("banana")
fruits.discard("grape")  # Remove if exists, no error if not

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))           # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))    # {3, 4}
print(set1.difference(set2))   # {1, 2}
print(set1.symmetric_difference(set2))  # {1, 2, 5, 6}

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}
```

---

## Object-Oriented Programming {#oop}

### Classes and Objects

```python
# Basic class definition
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())        # "Buddy says Woof!"
print(dog2.get_info())    # "Max is 5 years old"
print(Dog.species)        # "Canis familiaris"
```

### Inheritance

```python
# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def get_info(self):
        return f"{self.name} is a {self.species}"

# Child class
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed
    
    def make_sound(self):  # Method overriding
        return "Meow!"
    
    def purr(self):  # Additional method
        return f"{self.name} is purring"

# Using inheritance
cat = Cat("Whiskers", "Persian")
print(cat.make_sound())   # "Meow!"
print(cat.get_info())     # "Whiskers is a Cat"
print(cat.purr())         # "Whiskers is purring"
```

### Encapsulation

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):  # Getter method
        return self.__balance

account = BankAccount("12345", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)    # Error: cannot access private attribute
```

### Polymorphism

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 4), Circle(3), Rectangle(2, 2)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```

### Special Methods (Magic Methods)

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):  # String representation
        return f"{self.title} by {self.author}"
    
    def __len__(self):  # Length
        return self.pages
    
    def __eq__(self, other):  # Equality
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):  # Less than
        return self.pages < other.pages

book1 = Book("Python Guide", "John Doe", 300)
book2 = Book("Python Guide", "John Doe", 250)

print(book1)           # "Python Guide by John Doe"
print(len(book1))      # 300
print(book1 == book2)  # True
print(book1 < book2)   # False
```

---

## File Handling {#file-handling}

### Reading Files

```python
# Reading entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# Reading all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

### Writing Files

```python
# Writing to file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line\n")

# Appending to file
with open("output.txt", "a") as file:
    file.write("This line is appended\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### File Modes

```python
# "r" - Read mode (default for text)
# "w" - Write mode (overwrites existing file)
# "a" - Append mode
# "x" - Exclusive creation (fails if file exists)
# "b" - Binary mode (e.g., "rb", "wb")
# "t" - Text mode (default)
# "+" - Read and write (e.g., "r+", "w+")
```

---

## Error Handling {#error-handling}

### Try-Except Blocks

```python
# Basic error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")

# Try-Except-Else-Finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
finally:
    print("This always executes")
    # file.close() would go here if file was opened
```

### Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)

# Custom exceptions
class CustomError(Exception):
    pass

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds. Balance: {balance}, Required: {amount}"
        super().__init__(self.message)
```

---

## Modules and Packages {#modules}

### Creating and Using Modules

```python
# math_utils.py (module file)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

# main.py (using the module)
import math_utils

result = math_utils.add(5, 3)
print(result)

# Import specific functions
from math_utils import add, multiply
result = add(5, 3)

# Import with alias
import math_utils as mu
result = mu.multiply(4, 5)

# Import all (not recommended)
from math_utils import *
```

### Built-in Modules

```python
# math module
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
print(math.sin(math.pi/2))  # 1.0

# datetime module
from datetime import datetime, date, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

today = date.today()
print(today)

# random module
import random
print(random.randint(1, 10))        # Random integer
print(random.choice([1, 2, 3, 4]))  # Random choice
print(random.random())              # Random float 0-1

# os module
import os
print(os.getcwd())                  # Current directory
print(os.listdir('.'))              # List files
os.makedirs('new_folder', exist_ok=True)

# json module
import json
data = {"name": "John", "age": 30}
json_str = json.dumps(data)         # Convert to JSON string
data_dict = json.loads(json_str)    # Convert from JSON string
```

---

## List Comprehensions {#list-comprehensions}

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# With if-else
numbers = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(result)  # ['odd', 'even', 'odd', 'even', 'odd']

# Flattening a list
nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8]
```

---

## Lambda Functions {#lambda}

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Lambda with sorted
students = [("Alice", 25), ("Bob", 20), ("Charlie", 22)]
sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)  # [('Bob', 20), ('Charlie', 22), ('Alice', 25)]

# Lambda with reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
```

---

## Decorators {#decorators}

```python
# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Timing decorator
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()
```

---

## Generators {#generators}

```python
# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1

# Generator expression
squares = (x**2 for x in range(10))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Generator with send()
def number_generator():
    num = 0
    while True:
        received = yield num
        if received is not None:
            num = received
        else:
            num += 1

gen = number_generator()
print(next(gen))      # 0
print(next(gen))      # 1
print(gen.send(10))   # 10
print(next(gen))      # 11
```

---

## Best Practices

### Code Style (PEP 8)

```python
# Use meaningful variable names
user_name = "John"  # Good
un = "John"         # Bad

# Use snake_case for functions and variables
def calculate_total():
    pass

# Use PascalCase for classes
class UserAccount:
    pass

# Maximum line length: 79 characters
# Use 4 spaces for indentation (not tabs)
# Add blank lines between functions
```

### Documentation

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width
```

---

## Conclusion

This guide covers Python concepts from basics to intermediate level. Practice these concepts regularly and build projects to reinforce your learning. Python's simplicity and power make it an excellent language for beginners and professionals alike.

Happy coding!

