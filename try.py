import random

secret = random.randint(1, 100)
min_value = 1
max_value = 100
print(secret)

while True:
    guess = input(f"Make a guess between {min_value} and {max_value}: ")
    if int(guess) < min_value or int(guess) > max_value:
        print(f"Please enter a number between {min_value} and {max_value}.")
        continue    

    if int(guess) == secret:
        print(f"The secret is {secret}")
        break
    elif int(guess) < secret:
        print("Too low!")
        min_value = int(guess)
    elif int(guess) > secret:
        print("Too high!")
        max_value = int(guess)