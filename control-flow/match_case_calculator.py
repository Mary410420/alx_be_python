num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = int(num1) + int(num2)
        print("The result is " + str(result) + ".")
    case "-":
        result = int(num1) - int(num2)
        print("The result is " + str(result) + ".")
    case "*":
        result = int(num1) * int(num2)
        print("The result is " + str(result) + ".")
    case "/":
        if num2 == int(0):
            print("Cannot divide by zero.")
        else:
            result = int(num1) / int(num2)
            print("The result is " + str(result) + ".")
    case _:
        print("Invalid day entered.")