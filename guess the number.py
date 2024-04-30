#guess the number 
import random
n=random.randrange(1,50)
guess=int(input("Enter the number:"))
while n!=guess:
    if guess>n:
        print("Too high!!")
        guess=int(input("Enter the number"))
    elif guess<n:
        print("Too low")
        guess=int(input("Enter the number"))
    else:
        break
print("you guessed it right")
