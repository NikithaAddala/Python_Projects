import random

def guess(p,q):
    random_number = random.randint(p, q)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between {p} and {q}: "))
        if guess < random_number:
            print("Try a higher guess!")
        elif guess > random_number:
            print("Try a lower guess!")
    
    print(f"Hurrrraaaayyy!! Your guess {random_number} is correct!")

guess(int(input("Enter lower range: ")), int(input  ("Enter upper range: ")))