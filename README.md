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
