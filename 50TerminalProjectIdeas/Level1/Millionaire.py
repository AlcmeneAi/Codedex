money = 0

question1 = input("What is the capital of France?\nA) Berlin\nB) Madrid\nC) Paris\nD) Rome\nYour answer: ")

if question1.lower() == "c":
    money += 100
    print("Correct! You have $100.")
else :
    print("Wrong! The correct answer is C) Paris. You have $0.")
    exit()

question2 = input("What is 5 + 7?\nA) 10\nB) 12\nC) 14\nD) 15\nYour answer: ")

if question2.lower() == "b":
    money += 200
    print("Correct! You have $200.")
else :
    print("Wrong! The correct answer is B) 12. You have $0.")
    exit()

question3 = input("Which planet is known as the Red Planet?\nA) Earth\nB) Mars\nC) Jupiter\nD) Saturn\nYour answer: ")

if question3.lower() == "b":
    money += 300
    print("Correct! You have $300.")
else :
    print("Wrong! The correct answer is B) Mars. You have $0.")
    exit()

question4 = input("Who wrote 'Romeo and Juliet'?\nA) Charles Dickens\nB) Mark Twain\nC) William Shakespeare\nD) Jane Austen\nYour answer: ")

if question4.lower() == "c":
    money += 500
    print("Correct! You have $500.")
else :
    print("Wrong! The correct answer is C) William Shakespeare. You have $0.")
    exit()

question5 = input("What is the largest ocean on Earth?\nA) Atlantic Ocean\nB) Indian Ocean\nC) Arctic Ocean\nD) Pacific Ocean\nYour answer: ")
if question5.lower() == "d":
    money += 1000
    print("Correct! You have $1000.")
else :
    print("Wrong! The correct answer is D) Pacific Ocean. You have $0.")
    exit()

question6 = input("What is the chemical symbol for gold?\nA) Au\nB) Ag\nC) Fe\nD) Hg\nYour answer: ")
if question6.lower() == "a":
    money += 2000
    print("Correct! You have $2000")
else :
    print("Wrong! The correct answer is A) Au. You have $1000")
    exit()

question7 = input("Who painted the Mona Lisa?\nA) Vincent van Gogh\nB) Pablo Picasso\nC) Leonardo da Vinci\nD) Claude Monet\nYour answer: ")
if question7.lower() == "c":
    money += 4000
    print("Correct! You have $4000.")
else :
    print("Wrong! The correct answer is C) Leonardo da Vinci. You have $1000")
    exit()

question8 = input("What is the smallest prime number?\nA) 0\nB) 1\nC) 2\nD) 3\nYour answer: ")
if question8.lower() == "c":
    money += 8000
    print("Correct! You have $8000.")
else :
    print("Wrong! The correct answer is C) 2. You have $1000")
    exit()

question9 = input("Which element has the atomic number 1?\nA) Helium\nB) Hydrogen\nC) Oxygen\nD) Carbon\nYour answer: ")
if question9.lower() == "b":
    money += 16000
    print("Correct! You have $16000.")
else :
    print("Wrong! The correct answer is B) Hydrogen. You have $1000.")
    exit()

question10 = input("What is the hardest natural substance on Earth?\nA) Gold\nB) Iron\nC) Diamond\nD) Platinum\nYour answer: ")
if question10.lower() == "c":
    money += 32000
    print("Correct! You have $32000.")
else :
    print("Wrong! The correct answer is C) Diamond. You have $1000")
    exit()

question11 = input("Who is known as the 'Father of Computers'?\nA) Alan Turing\nB) Charles Babbage\nC) John von Neumann\nD) Steve Jobs\nYour answer: ")
if question11.lower() == "b":
    money += 64000
    print("Correct! You have $64000.")
else :
    print("Wrong! The correct answer is B) Charles Babbage. You have $32000.")
    exit()

question12 = input("What is the main ingredient in traditional Japanese miso soup?\nA) Tofu\nB) Seaweed\nC) Miso paste\nD) Rice\nYour answer: ")
if question12.lower() == "c":
    money += 125000
    print("Correct! You have $125000.")
else :
    print("Wrong! The correct answer is C) Miso paste. You have $32000.")
    exit()

question13 = input("Which country hosted the 2016 Summer Olympics?\nA) China\nB) Brazil\nC) UK\nD) Russia\nYour answer: ")
if question13.lower() == "b":
    money += 250000
    print("Correct! You have $250000.")
else :
    print("Wrong! The correct answer is B) Brazil. You have $32000.")
    exit()

question14 = input("What is the largest desert in the world?\nA) Sahara\nB) Arabian\nC) Gobi\nD) Antarctic\nYour answer: ")
if question14.lower() == "d":
    money += 500000
    print("Correct! You have $500000.")
else :
    print("Wrong! The correct answer is D) Antarctic. You have $32000.")
    exit()

question15 = input("Who developed the theory of relativity?\nA) Isaac Newton\nB) Nikola Tesla\nC) Albert Einstein\nD) Galileo Galilei\nYour answer: ")
if question15.lower() == "c":
    money += 1000000
    print("Correct! You are a millionaire with $1000000!")
else :
    print("Wrong! The correct answer is C) Albert Einstein. You have $32000.")
    exit()

print("Congratulations! You've answered all questions correctly and won $1000000!")