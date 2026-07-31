import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
guess = 0

print("I'm thinking of a number between 1 and 10.")

# Keep asking until the guess is correct
while guess != secret_number:
    # Convert input string to integer
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {secret_number}.")   