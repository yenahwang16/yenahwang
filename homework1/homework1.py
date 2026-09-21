# File: homework1.py

# --- 3.1 Variables and Data Types ---
a = 10
print(a)
print(type(a))
# a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b))
# b is a float, number with decimals

c = 3j
print(c)
print(type(c))
# c is a complex, mixture of a real part and an imaginary part

d = "hello"
print(d)
print(type(d))
# d is a string, used to represent textual data

e = [1, 2, 3]
print(e)
print(type(e))
# e is a list, used to store a collection of items in a single variable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a dictionary, used to store data in key-value pairs

g = (1, 2)
print(g)
print(type(g))
# g is a tuple, used to store an ordered, unchangeable collection of items

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list, used to store a collection of item in a single variable

i = True
print(i)
print(type(i))
# i is a boolean, can only hold one of two possible values

j = None
print(j)
print(type(j))
# j is a NoneType, only for constant None

k = [True, "blue", 12]
print(k)
print(type(k))
# k is a list, used to store a collection of item in a single variable

l = str(14)
print(l)
print(type(l))
# l is a string, used to represent textual data

m = 1e4
print(m)
print(type(m))
# m is a float, number with decimals

# Questions
# 1. I found nine different data types.
# 2. Integer, Float, Complex, String, List, Dictionary, Tuple, Boolean, and Nonetype
# 3. b, m: float / d, l: string / e, h ,k: list
# 4. str() makes it a string, which is different from an integer.
# 5. 

# --- 3.2 Booleans ---
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not equal or less than 9
print(bool("abc")) # True, a non-empty string is present
print(bool(123)) # True, a non-zero integer is present
print(bool(["apple", "cherry", "banana"])) # True, a non-empty list is present
print(bool(True)) # True, True is a Boolean value
print(bool(False)) # False, False is a Boolean value
print(bool(0)) # False, Boolean 0 is equal to false
print(bool("")) # False, an empty string is present
print(bool(" ")) # True, a non-empty string is present
print(bool(())) # False, an empty tuple is present
print(bool([])) # False, an empty list is present
print(bool({})) # False, an empty dictionary is present
print(bool(True and False)) # False, and requires both sides to be True
print(bool(True and True)) # True, and requires both sides to be True
print(bool(False and False)) # False, and requires both sides to be False
print(bool(True or False)) # True, only one side needs to be True
print(bool(True or True)) # True, only one side needs to be True
print(bool(False or False)) # False, only one side needs to be False
print(bool(not(False))) # True, the opposite of False is True
print(bool(not(True))) # False, the opposite of True is False

#Questions
# I realized that the Boolean value of anything empty is False, and with the non-empty, non-zero values are True. 
# I was surprised that bool(0) is identified as False, since it is a non-empty value, but a non-zero value.
# bool(3i+4K), True, since it is a non-empty value.
# bool(None), False, since it is a null state of the Python.

# --- 3.3.1 Arithmetic Operators ---
print(10+5) # 15, addition
print(10-5) # 5, subtraction
print(2*4) # 8, multiplication
print(6/3) # 2.0, division
print(5%2) # 1, modulus
print(3**2) # 9, exponentiation
print(15//2) # 7, floor division

# --- 3.3.2 Comparison Operators ---
print(5==2) # False, 5 is not equal to 2
print(10!=10) # False, 10 is equal to 10
print(2<5) # True, 2 is less than 5
print(12>5) # True, 12 is greater than 5
print(5<=6) # True, 5 is less than or equal to 6
print(1>=10) # False, 1 is not greater than or equal to 10

# --- 3.3.3 Assignment Operators ---
# x=5
# x+=5 # x=x+5, x=10
# x-=4 # x=x-4, x=1
# x*=3 # x=x*3, x=15

# --- 3.3.4 Logical Operators ---
# combine multiple conditional statements, bool(True and True) = True, bool(True and False) = False
# at least one condition is true. bool(True or False) = True, bool (False or False) = False
# it is the oppposite of the bool value. bool(not(True)) = False, bool(not(False)) = True

# 1. / asks you for the answer for the division in float, whiile // is asking how many times the divisor can fit into the dividend in integer
# 2. % is the remainder of the division, // is asking how many times the divisor can fit into the dividend in integer.
# 3. I will use %. ex) 5%2 = 1
# 4. x+=n -> x=x+n, x-=n -> x=x-n, x*=n -> x=x*n

# --- 3.4 Strings ---  
my_string = "hello" 
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints:el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string+" goodbye") # Prints: hello goodbye
print(my_string*7) # Prints: hellohellohellohellohellohellohello

# ---3.4.1 Questions ---
# 1. Slicing: taking a portion of a sequence and specifying in a range of positions, I used slicing for 8 and 9.
name = "Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski
name = "Oski"
print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski

# 4. f-string is a way to put variables directly into a string

# ---Terminal Commands---
# cd
# Change directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# List. Use it to see the contents of a directory
# Example: ls

# ls -a
# list all. Use it to see all contents of a directory
# Example: ls -a

# mkdir
# Make directory. Use it to create a new directory
# Example: mkdir new_folder

# cat
# Concatenate. Use it to view the contents of a file
# Example: cat file.txt

# pwd
# Print working directory. Use it to see the current directory you are in
# Example: pwd

# cd ..
# Change directory up one level. Use it to move up one level in the directory structure
# Example: cd ..

# cd .
# Change directory to the current directory. Use it to stay in the current directory
# Example: cd .

# cd ~
# Change directory to the home directory. Use it to move to the home directory
# Example: cd ~

# cp   
# Copy. Use it to copy files or directories
# Example: cp file.txt new_file.txt

# mv
# Move. Use it to move files or directories
# Example: mv file.txt new_folder/

# rm
# Remove. Use it to delete files or directories
# Example: rm file.txt

# clear
# Clear the terminal screen. Use it to clear the terminal screen
# Example: clear

# grep  
# Global regular expression print. Use it to search for a specific pattern in a file
# Example: grep "pattern" file.txt

# Questions:
# 1.
# python3
# Use it to run Python 3 scripts
# touch
# Create a new file. Use it to create a new file
# head
# View the first few lines of a file. Use it to see the beginning of a file

# 2. ls shows the contents of the current directory, while ls -a shows all content from the current directory

# 3. A hidden file is a file that is not normally visible when listing the contents of a directory. Hidden files are typically used to store configuration settings or other data that should not be modified by the user. In Unix-like operating systems, hidden files are usually prefixed with a dot (.) in their filename.

# 4. 
# ls -l: shows files in a detailed format with permissions
# ls -h: shows file sizes in a human-readable format
# ls -R: shows files in the current directory and all subdirectories recursively

