# print("Hello, World!")
# Importing the string_operations module
# import string_operations as so

# Sample strings and printing results
# sample_string = "hello World"

# print("Original:", sample_string)
# print("Reversed:", so.reverse_string(sample_string))
# print("Capitalized:", so.capitalize_string(sample_string))
# print("Lowercase:", so.lowercase_string(sample_string))
# print("Uppercase:", so.uppercase_string(sample_string))

# Importing modules from the utilities package
from utilities.calculator import add as add_def, subtract as subtract_def, multiply as multiply_def, divide as divide_def
from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

# Sample inputs and printing results using calculator.py
print("Using calculator.py:")
print("Addition:", add_def(10, 5))
print("Subtraction:", subtract_def(10, 5))
print("Multiplication:", multiply_def(10, 5))
print("Division:", divide_def(10, 5))

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))