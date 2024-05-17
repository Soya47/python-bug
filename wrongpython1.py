# Deliberately Wrong Python Code

# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

# Define a function to calculate the sum of a list of numbers
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Define a function to check if a string is a palindrome
def is_palindrome(s):
    reversed_str = s[::-1]
    if s == reversed_str:
        return True
    else:
        return False

# Define a class to represent a rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Define a function to print a triangle of stars
def print_triangle(height):
    for i in range(height):
        print("*" * i)

# Define a function to read numbers from a file and return their sum
def read_and_sum_numbers(filename):
    try:
        with open(filename, 'r') as file:
            numbers = file.readlines()
            numbers = [int(num) for num in numbers]
            return sum(numbers)
    except FileNotFoundError:
        print("File not found!")
        return None

# Define a function to calculate the Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

# Main function to demonstrate the buggy code
def main():
    # Calculate factorial of 5
    print("Factorial of 5:", factorial(5))

    # Check if 7 is prime
    print("Is 7 prime?", is_prime(7))

    # Sum numbers in a list
    numbers = [1, 2, 3, 4, 5]
    print("Sum of numbers:", sum_list(numbers))

    # Check if "radar" is a palindrome
    print("Is 'radar' a palindrome?", is_palindrome("radar"))

    # Calculate area of a rectangle
    rect = Rectangle(3, 4)
    print("Area of rectangle:", rect.area())

    # Print triangle of stars
    print_triangle(5)

    # Read numbers from a file and print their sum
    print("Sum of numbers in file:", read_and_sum_numbers("numbers.txt"))

    # Calculate Fibonacci sequence
    print("Fibonacci sequence:", fibonacci(10))

# Call the main function
if __name__ == "__main__":
    main()