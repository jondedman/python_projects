import time
import math
import random
# Practicing each of the essential Python concepts mentioned earlier is crucial for gaining proficiency. Here are some exercises and challenges tailored to specific concepts:

# 1. **Basic Syntax and Variables:**
#    - Write a Python program to calculate the area of a rectangle.
#    - Create a program that swaps the values of two variables without using a temporary variable.

def calculate_area(length=0, width=0):
    try:
        l = float(length)
        w = float(width)
        if l <= 0 or w <= 0:
            return 0
        else:
            return l * w
    except (ValueError, TypeError):
        return 0



# 2. **Data Types:**
#    - Create a program that converts temperatures between Fahrenheit and Celsius.

def temp_converter(temp, type="c"):
    try:
        if temp == "":
            raise ValueError("Please enter a number for the temperature")
        temp = int(temp)
        type = str(type).lower()
        if type == "c":
            result = (temp * 9/5) + 32
            new_type = "f"
        elif type == "f":
            result = (temp - 32) * 5/9
            new_type = "c"
        else:
            raise ValueError("Please enter 'c' or 'f' for the type")
        return f"{result} {new_type}"
    except TypeError:
        raise ValueError("Please enter a number for the temperature")


#    - Write a script that combines multiple strings into a single one.

def string_combiner(a="",b=""):
    return str(a) + str(b)

# 3. **Conditional Statements:**
#    - Build a simple calculator that performs addition, subtraction, multiplication, and division based on user input.

def calculator():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    operation = input("Enter an operation: ")
    result = 0
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    return result



#    - Write a program that determines whether a given number is even or odd.

def even_or_odd(num):
    try:
        num = int(num)
        if num % 2 == 0:
            return "even"
        else:
            return "odd"
    except ValueError:
        return "Please enter a number"

# 4. **Loops:**
#    - Implement a program to print the Fibonacci sequence up to a given number.
# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....it starts with 0 and 1, and the next number is the sum of the previous two numbers. The Fibonacci sequence is a good example of recursion and how to use it to solve problems.

def fibonacci(num):
    sequence = [0, 1]
    if num == 0:
        return [0]
    else:
        for x in range(1, num):
            result = sequence[-1] + sequence[x-1]
            sequence.append(result)
    return sequence





#         Sure! One way to approach this problem using recursion is to define a base case and a recursive case. The base case is the simplest case that can be solved without recursion, and the recursive case is the more complex case that requires recursion to solve.

# For the Fibonacci sequence, the base case is when the input is 0 or 1, because the sequence starts with 0 and 1. The recursive case is when the input is greater than 1, because the next number in the sequence is the sum of the previous two numbers.

# So, you can start by defining a function that takes an input n and returns the nth number in the Fibonacci sequence. Then, you can define the base case and the recursive case using conditional statements. Finally, you can call the function recursively with the previous two numbers in the sequence until you reach the base case.




#    - Write a script to find the factorial of a number using a `while` loop. an example of a factorial is 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(num):
    x = num -1
    while x > 0:
        num *= x
        x -= 1
    # print(num)


factorial(5)
# 5. **Functions:**
#    - Create a function that calculates the area of a circle based on its radius. the area of a circle is pi * r^2 where pi is 3.14159 and r is the radius of the circle.


def circle_area(r):
    area = math.pi * (r ** 2)
    return area
area = circle_area(5)
# print(area)




#    - Write a function to check if a given number is prime. A prime number is a number that is only divisible by 1 and itself except for 1 itself. For example, 2, 3, 5, 7, 11 are the first few prime numbers.

def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

# print(is_prime(11))

# optimised version:

def is_prime(num):
    if num < 2:
        return False
    for n in range(2, math.isqrt(num) + 1):
        if num % n == 0:
            return False
    return True



# 6. **Error Handling:**
#    - Build a program that handles exceptions when dividing by zero or performing invalid operations.
#    - Create a script that reads data from a file and handles potential file-related exceptions.

# 7. **File Handling:**
#    - Write a program that reads data from a file, processes it, and writes the results to a new file.
#    - Create a script that appends data to an existing file.

# 8. **Lists and List Comprehensions:**
#    - Implement a script that finds the largest and smallest elements in a list.
# step 1 remember the formula to create a list comprehension
# step 2 create a binary sort to find the largest ad smallest in a list or use min and max?

nums_list = random.sample(range(2, 100), 50) # generates a random list of 50 unique numbers
# nums_list.sort() - sorts the list
largest = max(nums_list)
smallest = min(nums_list)
# print(nums_list)
# print(largest)
# print(smallest)



#    - Use list comprehensions to generate a list of squares from 1 to 10.
squares = [num ** 2 for num in range(1, 11)]

# print(squares)

# 9. **Dictionaries:**
#    - Build a program that stores information about books in a dictionary and allows users to search for books by title or author.
# which info to store about book?

library = [
    {
        "Title": "Lord of the Rings",
        "Author": "Tolkien",
        "Year": 1950
    },

        {
        "Title": "1984",
        "Author": "Orwell",
        "Year": 1960
    }
]

print(library)




#    - Create a dictionary of students' grades and calculate the average grade.

# 10. **Modules and Libraries:**
#     - Use the `random` module to simulate a dice roll.
#     - Import the `math` module to calculate the square root of a number.

# 11. **Object-Oriented Programming (OOP):**
#     - Define a class representing a basic shape with methods to calculate area and perimeter for different shapes (e.g., rectangle, circle).
#     - Create a class for a simple bank account with methods to deposit, withdraw, and check the balance.

# 12. **String Manipulation:**
#     - Write a program that reverses a given string.
#     - Implement a function to count the occurrences of a specific word in a text.

# 13. **Math and Number Operations:**
#     - Build a program to calculate the sum of all even numbers in a given range.
#     - Write a script that computes the factorial of a number using a loop.

# 14. **List Sorting and Searching:**
#     - Create a script to sort a list of numbers in ascending and descending order.
#     - Implement a binary search algorithm to find an element in a sorted list.

# 15. **Recursion:**
#     - Write a recursive function to calculate the nth Fibonacci number.

def fibonacci2(num):
    if num < 2:
        return num
    else:
        return fibonacci2(num-1) + fibonacci2(num-2)


# This version use memoisation to improve the efficienty of the recursive fnction with a large number.
# This works by storing the results of previous function calls in a dictionary, so that they can be retrieved without having to call the function again.
def fibonacci3(n, memo={}):
    if n in memo:
        return memo[n]
    elif n < 2:
        return n
    else:
        result = fibonacci3(n -1, memo) + fibonacci3(n -2, memo)
        memo[n] = result
        return result

# print(fibonacci2(100))
# print(fibonacci3(10))




#     - Create a recursive function to calculate the factorial of a number. The factorial of a number is the product of all integers from 1 to that number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

def factorial(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

start_time = time.time()
# print(factorial(950))
end_time = time.time()
# print("Time for factorial with memoization: ", end_time - start_time)

def factorial2(num):
    if num == 0:
        return 1
    else:
        return num * factorial2(num -1)

start_time = time.time()
# print(factorial2(950))
end_time = time.time()
# print("Time for factorial without memoization: ", end_time - start_time)



# 16. **Data Structures and Algorithms:**
#     - Implement a stack or queue data structure.
#     - Write sorting algorithms like Bubble Sort or Quick Sort.

# 17. **Time and Date Manipulation:**
#     - Build a program that displays the current date and time.
#     - Calculate the number of days between two given dates.

# 18. **Regular Expressions:**
#     - Create a program that validates email addresses using regular expressions.
#     - Write a script that extracts all the URLs from a text using regular expressions.

# 19. **Exception Handling:**
#     - Handle exceptions when dividing by zero, and provide appropriate error messages.
#     - Create custom exceptions and use them in your code.

# 20. **Basic Input/Output:**
#     - Build a simple command-line calculator that takes user input for calculations.
#     - Create a program with a graphical user interface (GUI) that takes user input and displays results.

# 21. **Unit Testing:**
#     - Write unit tests for some of the functions or classes you've created in the previous exercises using a testing framework like `unittest` or `pytest`.

# 22. **Debugging Techniques:**
#     - Introduce intentional bugs in your code and practice debugging them using tools like `pdb` or print statements.

# 23. **Version Control:**
#     - Set up a Git repository for your coding exercises and practice committing, branching, and merging.

# 24. **Coding Style and PEP 8:**
#     - Ensure your code follows PEP 8 guidelines for code formatting and readability.


# print(area(5,6))
# print(string_combiner())
# print(temp_converter(32, "c"))
