def perform_operation(num1, num2, operation):
    num1= float(input("Enter the first number:"))
    num2= float(input("Enter the second number:"))
    operation=input("Enter operation (add, subtract, multiply, divide):").strip.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1*num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Error: division by zero is not allowed'
        else:
            num1/num2
    else:
        return "Error: unsupported operation. Please 'add', 'subtract', 'multiply', or 'divide'"
     




