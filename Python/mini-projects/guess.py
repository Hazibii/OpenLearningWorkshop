'''
Guess the number game
python3

'''
import random
o

number = random.randint(1,11)
guess = -1

print("Guess the number!")
while guess != number:
    guess = int(input("Is it..."))

    if guess == number:
        print("Hooray! you guess it right!")
    elif guess < number:
        print("Higer")
    elif guess > number:
        print("Smaller")
