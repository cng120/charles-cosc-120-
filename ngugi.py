#get the list of numbers between -100 and 0
def find_negative_numbers():
    negative_numbers = [i for i in range(-100, 0)]
    return negative_numbers
#get the list of numbers between 1 and 100 and the finf\d the list of odd numbers
def find_odd_numbers():
    odd_numbers = [i for i in range(1, 101) if i % 2 != 0]
    return odd_numbers
#you now use a function to display bpoth  the list of odd numbers and the list negative numbers
def display_combined_lists():
    negative_numbers = find_negative_numbers()
    odd_numbers = find_odd_numbers()
 #display the list negative numbers between -100 and 0   
    print("Negative numbers between -100 and 0:")
    print(negative_numbers)
#display the list of odd numbers between o and 100
    print("Odd numbers between 0 and 100:")
    print(odd_numbers)
#now display the combined list
# Call the function to display the combined lists
display_combined_lists()
