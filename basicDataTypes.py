
## BASIC DATA TYPES
'''
In programming, data types are fundamental concepts that define the nature of data
Computer systems need to interpret data in a way that is meaningful and 
useful. This involves understanding the different types of data that can be
processed and how they can be represented in a computer's memory.

A data type is a classification that specifies which type of value a 
variable can hold. In programming, data types are important because they 
determine the operations that can be performed on a particular piece of data. 
Common data types include integers, floating-point numbers, strings, and 
booleans.

Python offers raw data types to allow data to be assigned to variables or
constants. The five main types which are classed as literals includes;
1. Numeric (Integer, Float, Complex Numbers)
2. Sequence (String, List, Tuple)
3. Dictionary (Key-Value Pairs)
4. Set (Unique Unordered Collection)
5. Boolean (True or False)

In programming, you need to decide what type would best suit your data and 
the operations you want to perform on it. Choosing the right data type is 
crucial for optimizing performance and ensuring the correctness of your code.
'''

# Numeric Data Types
'''Numeric data types are used to represent numbers in programming. 
Python supports several numeric types, including integers, floating-point numbers,
and complex numbers. Each type has its own characteristics and use cases.
'''
# 1. Integer
'''Integers are whole numbers, both positive and negative, without any decimal 
point. They can be used for counting, indexing, and performing arithmetic operations.'''
x = 10
print(x)

a = 5
b = 3
print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication

# 2. Float
'''Floating-point numbers are used to represent real numbers with decimal points.
They are useful for representing values that require precision, such as measurements or financial calculations.'''
pi = 3.14
print(pi)

# 3. Complex Numbers
'''
Complex numbers are represented as a real part and an imaginary part.
In Python, complex numbers are written as `a + bj`, where `a` is  the real part and `b` is the imaginary part.    
complex_num = 2 + 3j
'''
complex_num = 2 + 3j
print(complex_num.real)  # Accessing the real part
print(complex_num.imag)  # Accessing the imaginary part

# Sequence Data Types
'''Sequence data types are used to store collections of items in a specific order.
Python provides several sequence types, including strings, lists, and tuples.
'''
# 1. String
'''Strings are used to represent text data. They are sequences of characters enclosed in quotes.
Strings can be manipulated using various methods, such as concatenation, slicing, and formatting.'''
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# 2. List
'''Lists are ordered collections of items that can be of different data types.
They are mutable, meaning you can change their contents after creation. 
Lists are defined using square brackets [].'''

fruits = ["apple", "banana", "cherry"]
print(fruits)

# 3. Tuple
'''Tuples are similar to lists but are immutable, meaning their contents cannot be changed after creation.
Tuples are defined using parentheses ().'''

coordinates = (10.5, 20.3)
print(coordinates)

#Dictionary Data Type
'''Dictionaries are used to store key-value pairs, where each key is unique and maps to a specific value.
Dictionaries are defined using curly braces {}. They are useful for representing structured data.'''
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Set Data Type
'''Sets are unordered collections of unique items. They are useful for storing distinct values and performing 
set operations like union, intersection, and difference.'''
# Example of a set
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

# Boolean Data Type
'''Booleans represent truth values, either True or False. They are often used in conditional statements and logical operations.'''
is_active = True


