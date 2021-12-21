# Nerd Challenge: Debugging
# Erm, I found some bugs :(
import random

guess = input('Guess a number between 1 and 5: ')
x = random.randint(0, 5)

print(f"You guessed {guess}")
print(f"The answer was: {x}")

if guess == x:
    print("Congrats you guessed right!")
else:
    print("Sorry you guessed wrong. You lose.")

random_fact_result = guess / x
print(f"Random fact of the day: Your guess number, {guess} divided by the answer {x} is equal to {random_fact_result}")

