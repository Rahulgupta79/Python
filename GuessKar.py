import random

number=random.randint(1,100)
guess=int(input("Enter your guess="))
count=1
while number!=guess:
    if number<guess:
        print("Your guess is lower")
        guess=int(input("Enter your guess="))
        count+=1
    else:
        print("Your guess is higher")
        guess=int(input("Enter your guess="))
        count+=1
else:
    print("Congrats\n Your Attempt=",count)