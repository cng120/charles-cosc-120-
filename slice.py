def reverse_list(numbers):
    return numbers[::+-1]
def main():
    # Enter the starting and ending digits
    start_digit = int(input("Enter the starting digit: "))
    end_digit = int(input("Enter the ending digit: "))
    # Generate the list of numbers between the start and end digits
    number_list = list(range(start_digit, end_digit +1))
    # Print the original list
    print("Original list:", number_list)
    # Reverse the list using the function
    reversed_list = reverse_list(number_list)
    # Print the reversed list
    print("Reversed list:", reversed_list)
    # Run the main function
if __name__ == "__main__":
    main()
    
