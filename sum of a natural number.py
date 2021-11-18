num = int(input("enter the number >> "))

if num < 0:
    print("enter the positive number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
        print('the sum is = ',sum)




#by another formula

n = int(input("number"))
sum = n*(n+1)/2
print(sum)