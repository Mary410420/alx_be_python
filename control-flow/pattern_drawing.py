size = int(input("Enter the size of the pattern:"))
x = size

while x > 0:
    for num in range(size):
        print("*", end="")
    print()
    x -= 1