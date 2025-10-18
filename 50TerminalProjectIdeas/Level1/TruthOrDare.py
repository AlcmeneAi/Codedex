print("Welcome to Truth or Dare!")
print("Type 'truth' for a truth question or 'dare' for a dare.")
print("Type 'quit' to exit the game.")

answer = input("Your choice (truth/dare/quit): ").strip().lower()

import random 

truth_questions = [
    "What is your biggest fear?",
    "What is your most embarrassing moment?",
    "Have you ever lied to your best friend?",
    "What is a secret you have never told anyone?",
    "What is your guilty pleasure?"
]

dare_challenges = [
    "Do 10 push-ups.",
    "Sing a song loudly.",
    "Dance for 30 seconds.",
    "Do an impression of your favorite celebrity.",
    "Talk in a funny accent for the next 5 minutes."
]

if answer == 'truth':
    question = random.choice(truth_questions)
    print(f"Truth: {question}")
    answer_input = input("Your answer: ")
    print("Thank you for your honesty!")
elif answer == 'dare':
    challenge = random.choice(dare_challenges)
    print(f"Dare: {challenge}")
    input("Press Enter after you complete your dare...")
    print("Well done on completing your dare!")
elif answer == 'quit':
    print("Thanks for playing! Goodbye!")
else:
    print("Invalid choice. Please type 'truth', 'dare', or 'quit'.")

