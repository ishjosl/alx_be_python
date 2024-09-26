number1 = input("Enter the first number:")
number2 = input("Enter the second number:")

operation = input("Choose the operation (+, -, *, /):")
result= None

match operation:
    case '+':
        result= number1+number2
    case '-':
        result= number1-number2
    case '*':
        result= number1*number2
    case '/':
        if number2==0:
            result = "Error: Division by zero is not allowed"
        else:
            result= number1/number2
    case '_':
        result = "Invalid operation"

print(f"The result is: {result}")
