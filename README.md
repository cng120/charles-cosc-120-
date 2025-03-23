# Reverse List Program

This Python program generates a list of numbers within a specified range and reverses the list using a custom function.

## Features

- Accepts user input for the starting and ending digits.
- Generates a list of numbers within the specified range.
- Reverses the list using slicing.

## How to Use

1. Run the program.
2. Enter the starting digit when prompted.
3. Enter the ending digit when prompted.
4. The program will display the original list and the reversed list.

### Example

```plaintext
Enter the starting digit: 1
Enter the ending digit: 5
Original list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]
```

## Code Explanation

- **`reverse_list(numbers)`**: A function that takes a list of numbers and returns the reversed list using slicing.
- **`main()`**: The main function that:
  - Accepts user input for the range.
  - Generates the list of numbers.
  - Prints the original and reversed lists.

## How to Run

1. Save the code in a file, e.g., `reverse_list.py`.
2. Run the file using Python:
   ```sh
   python reverse_list.py
   ```
Geometry Calculator
This program is a simple geometry calculator that allows users to calculate the area and perimeter/circumference of various shapes. The program runs in a loop until the user decides to exit.

Features
The program provides the following options:

Area and Circumference of a Circle

Input: Radius of the circle
Output: Area and circumference of the circle
Area and Perimeter of a Triangle

Input: Base, height, and hypotenuse of the triangle
Output: Area and perimeter of the triangle
Area and Perimeter of a Rectangle

Input: Width and length of the rectangle
Output: Area and perimeter of the rectangle
Exit

Exits the program.
How to Use
Run the program in a Python environment.
Choose an option from the menu by entering the corresponding number (1, 2, 3, or 4).
Follow the prompts to input the required dimensions for the selected shape.
View the calculated results.
To exit the program, select option 4.
Example Usage
Choose any of the three options
1. Area and circumference of a circle
2. Area and perimeter of a triangle
3. Area and perimeter of a rectangle
4. Exit
Choose among the choices: 1
Enter radius of the circle: 5
Area of the circle: 78.53981633974483
Circumference of the circle: 31.41592653589793

Requirements
Python 3.x
math module (for pi constant)
Notes
Ensure that all inputs are valid numbers.
If an invalid option is selected, the program will prompt the user to choose again.
License
This program is provided as-is for educational purposes. Feel free to modify and use it as needed.



# Number List Generator and Display

This Python script generates and displays two lists of numbers:
1. A list of negative numbers between -100 and 0.
2. A list of odd numbers between 1 and 100.

The script is structured into three functions:
- `find_negative_numbers()`
- `find_odd_numbers()`
- `display_combined_lists()`

## Features

1. **Generate Negative Numbers**  
   The `find_negative_numbers()` function creates a list of all integers from -100 to -1 using Python's `range()` function.

2. **Generate Odd Numbers**  
   The `find_odd_numbers()` function generates a list of odd integers between 1 and 100 by filtering numbers using the modulus operator (`%`).

3. **Display Combined Lists**  
   The `display_combined_lists()` function calls the above two functions to generate the lists and then prints them to the console.

## Code Overview

### `find_negative_numbers()`
This function generates a list of negative numbers between -100 and 0:
```python
def find_negative_numbers():
    negative_numbers = [i for i in range(-100, 0)]
    return negative_numbers
find_odd_numbers()
This function generates a list of odd numbers between 1 and 100:
def display_combined_lists():
    negative_numbers = find_negative_numbers()
    odd_numbers = find_odd_numbers()
    print("Negative numbers between -100 and 0:")
    print(negative_numbers)
    print("Odd numbers between 0 and 100:")
    print(odd_numbers)
Main Execution
The script calls the display_combined_lists() function to display the results:


display_combined_lists()
How to Run
Save the script to a file, e.g., number_list_generator.py.
Run the script using Python:
python number_list_generator.py
Example Output
When you run the script, you will see the following output:
Negative numbers between -100 and 0:
[-100, -99, -98, ..., -2, -1]
Odd numbers between 0 and 100:
[1, 3, 5, ..., 97, 99]
Requirements
Python 3.x
Notes
The script uses list comprehensions for concise and efficient list generation.
The range() function is used to define the range of numbers for both negative and odd lists.
Feel free to modify the script to generate other ranges or types of numbers! ```
