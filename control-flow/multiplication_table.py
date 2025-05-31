nunmber = int(input("Enter a number to see its multiplication table:"))

for num in range(1, 11):
    x = str(nunmber)
    y = str(num)
    z = str(nunmber * num)
    print( x + " * " + y + " = " + z)