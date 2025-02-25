
def find_negative_numbers():
    negative_numbers = [i for i in range(-100, 0)]
    return negative_numbers

def find_odd_numbers():
    odd_numbers = [i for i in range(1, 101) if i % 2 != 0]
    return odd_numbers

def display_combined_lists():
    negative_numbers = find_negative_numbers()
    odd_numbers = find_odd_numbers()
    
    print("Negative numbers between -100 and 0:")
    print(negative_numbers)
    
    print("Odd numbers between 0 and 100:")
    print(odd_numbers)

# Call the function to display the combined lists
display_combined_lists()
