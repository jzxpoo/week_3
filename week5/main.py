# main.py - Main program for the cafe billing system
# This file handles user input and orchestrates the billing process

# Import the functions from utils.py
from utils import calculate_total, print_receipt

def main():
    """
    Main function that runs the cafe billing program.
    Gets user input, calculates the total, and displays the receipt.
    """
    # Display a welcome message
    print("=== Cafe Billing System ===")
    print()
    
    # Get input from the user
    # Using input() function to collect data from the keyboard
    customer_name = input("Enter customer name: ")
    
    # Get item quantities
    # int() converts the string input to an integer
    coffee_qty = int(input("Enter coffee quantity: "))
    tea_qty = int(input("Enter tea quantity: "))
    sandwich_qty = int(input("Enter sandwich quantity: "))
    
    print()  # Print a blank line for spacing
    
    # Calculate the total bill using the imported function
    total = calculate_total(coffee_qty, tea_qty, sandwich_qty)
    
    # Print the receipt using the imported function
    # Pass all the necessary data to the print_receipt function
    print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total)


# This is the standard Python idiom to check if the script is being run directly
# (as opposed to being imported as a module)
if __name__ == "__main__":
    # Call the main function to start the program
    main()