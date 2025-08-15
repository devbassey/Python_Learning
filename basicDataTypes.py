'''
BASIC DATA TYPES
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