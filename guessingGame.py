import random
number = random.randint(1,9)
tries = 0

while tries < 5: 
    
    guess = int(input("the number is between 1,9: "))
    if guess > number:
        print('too high, try again')
    if guess < number:
        print('too low, try again')
    if guess == number:
        break
if guess == number:
    print("CONGRADULATIONS YOU WON!!!")
elif guess != number:
    print("You lost, the number was ", number)

    
