num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

type_of_operation = input("Choose the operation (+, -, *, /):")

if type_of_operation == "+":
    result = int(num1) + int(num2)
    print("The result is " + str(result) + ".")
elif type_of_operation == "-":
    result = int(num1) - int(num2)
    print("The result is " + str(result) + ".")
elif type_of_operation == "*":
    result = int(num1) * int(num2)
    print("The result is " + str(result) + ".")
elif type_of_operation == "/":
    if num2 == int(0):
        print("Cannot divide by zero.")
    else:
        result = int(num1) / int(num2)
        print("The result is " + str(result) + ".")