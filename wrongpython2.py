# Intentionally Flawed Python Code

# Define a function to calculate the average of a list of numbers
def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Define a function to check if a number is even
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Define a function to convert a string to uppercase
def to_uppercase(s):
    return s.upper()

# Define a function to find the maximum element in a list
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Define a function to check if a list is sorted
def is_sorted(numbers):
    sorted_numbers = sorted(numbers)
    if numbers == sorted_numbers:
        return True
    else:
        return False

# Define a function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Define a function to reverse a string
def reverse_string(s):
    return s[::-1]

# Main function to demonstrate the buggy code
def main():
    # Calculate average of numbers
    numbers = [1, 2, 3, 4, 5]
    print("Average of numbers:", average(numbers))

    # Check if 6 is even
    print("Is 6 even?", is_even(6))

    # Convert string to uppercase
    s = "hello"
    print("Uppercase:", to_uppercase(s))

    # Find maximum element in list
    print("Max number:", find_max(numbers))

    # Check if list is sorted
    print("Is list sorted?", is_sorted(numbers))

    # Calculate factorial of 5
    print("Factorial of 5:", factorial(5))

    # Reverse a string
    print("Reversed string:", reverse_string("hello"))

# Call the main function
if __name__ == "__main__":
    main()
