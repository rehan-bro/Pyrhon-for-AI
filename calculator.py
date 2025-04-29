print("Welcome to the calculator program!")

operation = input("Please enter the operation you want to perform (+, -, *, /): ")
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))

if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {round(result,3)}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {round(result,3)}")    
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {round(result,3)}")    
elif operation == "/":  
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {round(result,3)}")
    else:
        print("Error: Division by zero is not allowed.")
        
else:
    print(f"{operation} is not a valid operation. Please enter +, -, *, or /.")
# The calculator program allows the user to perform basic arithmetic operations: addition, subtraction, multiplication, and division.   