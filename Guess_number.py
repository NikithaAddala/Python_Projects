import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low. Try another guess!")
        elif guess > random_number:
            print("Too high. Try another guess!")
    
    print(f"Your guess {random_number} is correct ")

guess(int(input("Enter range: ")))