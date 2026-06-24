# Student_Ave_Calc.py

while True:
    # Input
    quiz1 = float(input("Enter Quiz 1 mark: "))
    quiz2 = float(input("Enter Quiz 2 mark: "))
    quiz3 = float(input("Enter Quiz 3 mark: "))

    # Process
    average = (quiz1 + quiz2 + quiz3) / 3

    # Output
    print("\nAverage Mark:", round(average, 2))

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # Ask for another student
    again = input("\nEnter another student's marks? (yes/no): ").lower()

    if again != "yes":
        print("Program Ended.")
        break