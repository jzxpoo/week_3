# Week 5 - Tutorial 5 Documentation

## ACTIVITY 1:

### 1.1 Define the Problem Statement
A small cafe needs an automated program to calculate customer bills and print receipts instead of doing manual calculations.

### 1.2 What are the Inputs?
- Customer name (string)
- Coffee quantity (integer)
- Tea quantity (integer)  
- Sandwich quantity (integer)

### 1.3 What are the Outputs?
A formatted receipt showing:
- Customer name
- Quantities of each item
- Total bill in RM (with 2 decimal places)

### 1.4 What would be the Typical Process Flow?
1. Display welcome message
2. Get customer name
3. Get coffee quantity
4. Get tea quantity
5. Get sandwich quantity
6. Calculate total = (coffee × 8.50) + (tea × 6.00) + (sandwich × 12.00)
7. Display receipt with all details and total

### 1.5 What are the Constraints?
- Fixed prices: Coffee = RM 8.50, Tea = RM 6.00, Sandwich = RM 12.00
- Quantities must be non-negative integers
- Total shown in RM with 2 decimal places
- Logic functions in utils.py, main program in main.py

---

## ACTIVITY 2: Problem Decomposition

The problem is broken into 3 main tasks:

1. **Input Collection** - Get customer name and item quantities (in main.py)
2. **Bill Calculation** - Calculate total using fixed prices (in utils.py)
3. **Receipt Display** - Print formatted receipt (in utils.py)

---

## ACTIVITY 3: Pseudocode

START
PRINT "Enter customer name:"
INPUT customer_name
PRINT "Enter coffee quantity:"
INPUT coffee_quantity
PRINT "Enter tea quantity:"gi
INPUT tea_quantity
PRINT "Enter sandwich quantity:"
INPUT sandwich_quantity
total = (coffee quantity * 8.50) + (tea quantity * 6.00) + (sandwich quantity * 12.00)
PRINT "========== RECEIPT =========="
PRINT "Customer : " + customer_name
PRINT "Coffee : " + coffee_quantity
PRINT "Tea : " + tea_quantity
PRINT "Sandwich : " + sandwich_quantity
PRINT "TOTAL = RM " + total
END