import random 

print("Welcome to 'Guess My Number'!")
print("-"*30)

print("User Instructions:")
print("1. The computer will randomly select a number between 1 and 100.")
print("2. You have to guess the number.")
print("3. After each guess, you will be told if the actual number is higher or lower.")
print("-"*30)

number_to_guess = random.randint(1, 100)
guess = None
attempts = 0

while guess != number_to_guess:
    guess = int(input("Enter your guess (between 1 and 100): "))
    attempts += 1
    
    if guess < number_to_guess:
        print("Higher!")
    elif guess > number_to_guess:
        print("Lower!")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        print("-"*30)

        