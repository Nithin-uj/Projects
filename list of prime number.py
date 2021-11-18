lower = int(input("enter the minimum prime number >> "))
upper = int(input("enter the maximum prime number >> "))

print ("prime numbers between between",lower,"and",upper,"are")

for num in range(lower, upper + 1):
    if num > 1 :
        for i in range(2,num):
            if (num % i) == 0:
                break
        else :
            print(num)