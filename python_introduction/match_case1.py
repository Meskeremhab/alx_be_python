import random

while True:
    secret_number = random.randint(1, 10)
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))

    if guess == secret_number:
        print("Congratulations, you guessed it!")
    elif guess > secret_number:
        print("Oops, your guess is a bit high. Try again!")
        guess = int(input("Second try: "))
        if guess == secret_number:
            print("Congratulations, you guessed it!")
        else:
            print(f"Sorry, the correct number was {secret_number}.")
    else:
        print("Nope, your guess is a bit low. Give it another shot!")
        guess = int(input("Second try: "))
        if guess == secret_number:
            print("Congratulations, you guessed it!")
        else:
            print(f"Sorry, the correct number was {secret_number}.")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
