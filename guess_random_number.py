import random

def guess(x):
    random_number=random.randint(1,x)
    guess = 0
    while guess !=random_number:
        guess = int(input('Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print("Try higher")
        elif guess > random_number:
            print("Try lower")
        
            
    print("Good job!")      
  
guess(10)
