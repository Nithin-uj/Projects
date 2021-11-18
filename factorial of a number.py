num = int(input("enter the number to calculate its factorial >> "))

factorial = 1
if num < 0:
  print("sorry, factorial doesnot exist")
elif num == 0:
    print("factorial of ",num,"is",factorial)
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print("The factorial of",num,"is",factorial)