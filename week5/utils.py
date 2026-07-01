# utils.py - Contains helper functions for the cafe billing system

# Function to calculate the total bill
def calculate_total(coffee_qty, tea_qty, sandwich_qty):
    """
    Calculate the total cost of the order based on item quantities.
    
    Parameters:
    coffee_qty (int): Number of coffees ordered
    tea_qty (int): Number of teas ordered  
    sandwich_qty (int): Number of sandwiches ordered
    
    Returns:
    float: Total cost in RM
    """
    # Define the fixed prices for each item
    COFFEE_PRICE = 8.50  # Price per coffee in RM
    TEA_PRICE = 6.00     # Price per tea in RM
    SANDWICH_PRICE = 12.00  # Price per sandwich in RM
    
    # Calculate total by multiplying quantity by price for each item
    # and then adding them all together
    total_coffee = coffee_qty * COFFEE_PRICE
    total_tea = tea_qty * TEA_PRICE
    total_sandwich = sandwich_qty * SANDWICH_PRICE
    
    # Sum up all the item totals
    total = total_coffee + total_tea + total_sandwich
    
    # Return the final total
    return total


# Function to print the receipt
def print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total):
    """
    Print a formatted receipt showing the customer's order and total.
    
    Parameters:
    customer_name (str): Name of the customer
    coffee_qty (int): Number of coffees ordered
    tea_qty (int): Number of teas ordered
    sandwich_qty (int): Number of sandwiches ordered
    total (float): Total cost of the order
    """
    # Print the receipt header
    print("========== RECEIPT ==========")
    
    # Print customer information
    print(f"Customer : {customer_name}")
    
    # Print item quantities
    print(f"Coffee : {coffee_qty}")
    print(f"Tea : {tea_qty}")
    print(f"Sandwich : {sandwich_qty}")
    
    # Print separator line
    print("------------------------------")
    
    # Print the total with proper formatting (2 decimal places)
    print(f"TOTAL = RM {total:.2f}")