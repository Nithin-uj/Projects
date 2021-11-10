print("Enter two numbers to find its LCM")
x = int(input("enter the first number >> "))
y = int(input("enter the second number >> "))

if x > y:
    greater = x
else:
    greater = y

while(True):
    if ((greater % x == 0) & (greater % y == 0)):
        lcm = greater
        break
    greater +=1
print(f"lcm of {x} and {y} is {lcm}")

