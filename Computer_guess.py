import random

def computer_guess(low, high):
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c)?")
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'{guess} is correct!')

computer_guess(int(input("Enter lower range: ")),int(input("Enter upper range: ")))