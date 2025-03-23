def find_largest_and_smallest(numbers):
    # Find the largest and smallest numbers using the built-in functions
    largest = max(numbers)
    smallest = min(numbers)
    
    return largest, smallest

# Prompt user to enter a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = [int(num) for num in user_input.split()]

# Check if the list is empty
if len(numbers) == 0:
    print("The list is empty. Please enter at least one number.")
else:
    # Find the largest and smallest numbers
    largest, smallest = find_largest_and_smallest(numbers)

    # Print the results
    print("Largest number:", largest)
    print("Smallest number:", smallest)
