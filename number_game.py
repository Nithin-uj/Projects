import random

secretnum = random.randint(1,20)
print(secretnum)

count = 1

while(True):
    guess = int(input("Guess the number (1-20) >> "))
    if guess == secretnum:
        print("Correct!....VICTORY")
        break
    else:
        print("on no! Try again")
        count+=1

print("You Took ",count," chances")
