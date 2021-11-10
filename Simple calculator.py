print("Simple Calculator")
print("select an option")

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("0. End the program")

while True:
    operation = int(input("Enter the choice(1/2/3/4/0) >> "))

    if operation == 1:
        num1 = float(input("Enter the num1>> "))
        num2 = float(input("Enter the num2>> "))
        print(num1+num2)
    elif operation == 2:
        num1 = float(input("Enter the num1>> "))
        num2 = float(input("Enter the num2>> "))
        print(num1-num2)
    elif operation == 3:
        num1 = float(input("Enter the num1>> "))
        num2 = float(input("Enter the num2>> "))
        print(num1 * num2)
    elif operation == 4:
        num1 = float(input("Enter the num1>> "))
        num2 = float(input("Enter the num2>> "))
        print(num1 // num2)
    elif operation == 0:
        break
    else:
        print("Invalid option")
