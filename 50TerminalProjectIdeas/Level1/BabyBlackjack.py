import random

print("Welcome to Baby Blackjack!")
print("-"*30)

player_numbers = random.randint(1, 10) , random.randint(1, 10)
dealer_numbers = random.randint(1, 10) , random.randint(1, 10)

print(f"Your numbers are {player_numbers}")
print(f"Dealer's numbers are {dealer_numbers}")
print("-"*30)

total_player = sum(player_numbers)
total_dealer = sum(dealer_numbers)


if total_player > total_dealer:
    print(f"You win! Your total: {total_player}, Dealer's total: {total_dealer}")
elif total_player < total_dealer:
    print(f"You lose! Your total: {total_player}, Dealer's total: {total_dealer}")
else:
    print(f"It's a tie! Your total: {total_player}, Dealer's total: {total_dealer}")