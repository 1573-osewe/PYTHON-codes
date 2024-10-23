import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congrats! You guessed it in {attempts} attempts.")
            break

guessing_game()
