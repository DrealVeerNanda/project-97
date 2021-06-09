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
    
    tries = tries + 1
if guess == number:
    print("CONGRADULATIONS YOU WON!!!")
else:
    print("You lost, the number was ", number)

    
