import random

print("Choose your weapon!")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

user_choice = input("Enter the number of your choice:  ")

computer = random.randint(1, 3)

if user_choice == "1":
    if computer == 1:
        print("Computer chose Rock. It's a tie!")
    elif computer == 2:
        print("Computer chose Paper. You lose!")
    elif computer == 3:
        print("Computer chose Scissors. You win!")
elif user_choice == "2":
    if computer == 1:
        print("Computer chose Rock. You win!")
    elif computer == 2:
        print("Computer chose Paper. It's a tie!")
    elif computer == 3:
        print("Computer chose Scissors. You lose!")
elif user_choice == "3":
    if computer == 1:
        print("Computer chose Rock. You lose!")
    elif computer == 2:
        print("Computer chose Paper. You win!")
    elif computer == 3:
        print("Computer chose Scissors. It's a tie!")
else:
    print("Invalid input! Please choose 1, 2, or 3.")
