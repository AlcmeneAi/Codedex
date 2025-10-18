import random

print("Choose your weapon!")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Lizard")
print("5. Spock")

user_choice = input("Enter the number of your choice:  ")

computer = random.randint(1, 5)

if user_choice == "1":
    if computer == 1:
        print("Computer chose Rock. It's a tie!")
    elif computer == 2:
        print("Computer chose Paper. You lose!")
    elif computer == 3:
        print("Computer chose Scissors. You win!")
    elif computer == 4:
        print("Computer chose Lizard. You win!")
    elif computer == 5:
        print("Computer chose Spock. You lose!")
elif user_choice == "2":
    if computer == 1:
        print("Computer chose Rock. You win!")
    elif computer == 2:
        print("Computer chose Paper. It's a tie!")
    elif computer == 3:
        print("Computer chose Scissors. You lose!")
    elif computer == 4:
        print("Computer chose Lizard. You lose!")
    elif computer == 5:
        print("Computer chose Spock. You win!")
elif user_choice == "3":
    if computer == 1:
        print("Computer chose Rock. You lose!")
    elif computer == 2:
        print("Computer chose Paper. You win!")
    elif computer == 3:
        print("Computer chose Scissors. It's a tie!")
    elif computer == 4:
        print("Computer chose Lizard. You win!")
    elif computer == 5:
        print("Computer chose Spock. You lose!")
elif user_choice == "4":
    if computer == 1:
        print("Computer chose Rock. You lose!")
    elif computer == 2:
        print("Computer chose Paper. You win!")
    elif computer == 3:
        print("Computer chose Scissors. You lose!")
    elif computer == 4:
        print("Computer chose Lizard. It's a tie!")
    elif computer == 5:
        print("Computer chose Spock. You win!")
elif user_choice == "5":
    if computer == 1:
        print("Computer chose Rock. You win!")
    elif computer == 2:
        print("Computer chose Paper. You lose!")
    elif computer == 3:
        print("Computer chose Scissors. You win!")
    elif computer == 4:
        print("Computer chose Lizard. You lose!")
    elif computer == 5:
        print("Computer chose Spock. It's a tie!")
else:
    print("Invalid input! Please choose 1, 2, 3, 4, or 5.")