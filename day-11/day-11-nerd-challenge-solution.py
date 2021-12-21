# Nerd Challenge: Debugging
# Erm, I found some bugs :(
import random

guess = input('Guess a number between 1 and 5: ')
if guess.isdigit() and 5 >= int(guess) >= 1:
    guess = int(guess)
else:
    print("Sorry, next time enter a number between 1 and 5")
    exit(-1)

x = random.randint(1, 5)

print(f"You guessed {guess}")
print(f"The answer was: {x}")

if guess == x:
    print("Congrats you guessed right!")
else:
    print("Sorry you guessed wrong. You lose.")

random_fact_result = guess / x
print(f"Random fact of the day: Your guess number, {guess} divided by the answer {x} is equal to {random_fact_result}")

# Error #1: input returns a string. We need to compare integers!
# Error #2: The instructions say between 1 and 5, but 0 is possible
# Error #3: ZeroDivisionError Exception
# Error #4: TypeError: unsupported operand type(s) for /: 'str' and 'int'
