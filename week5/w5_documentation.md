START
    DISPLAY "Enter customer name:"
    INPUT customer_name
    DISPLAY "Enter coffee quantity:"
    INPUT coffee_qty
    DISPLAY "Enter tea quantity:"
    INPUT tea_qty
    DISPLAY "Enter sandwich quantity:"
    INPUT sandwich_qty
    
    total = (coffee_qty * 8.50) + (tea_qty * 6.00) + (sandwich_qty * 12.00)
    
    DISPLAY "========== RECEIPT =========="
    DISPLAY "Customer : " + customer_name
    DISPLAY "Coffee : " + coffee_qty
    DISPLAY "Tea : " + tea_qty
    DISPLAY "Sandwich : " + sandwich_qty
    DISPLAY "------------------------------"
    DISPLAY "TOTAL = RM " + total
END