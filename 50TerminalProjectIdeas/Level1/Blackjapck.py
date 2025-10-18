print("Welcome to Blackjack!")
print("-"*30)

import random

player_cards = random.randint(1, 11) , random.randint(1, 11)

print(f"Your cards are {player_cards}")

sum_player = sum(player_cards)

print(f"Your total is {sum_player}")
print("-"*30)

answer = input("Do you want another card? (y/n): ").lower()

if answer == 'y':
    new_card = random.randint(1, 11)
    player_cards += (new_card,)
    sum_player = sum(player_cards)
    print(f"Your new card is {new_card}")
    print("-"*30)
    print(f"Your cards are now {player_cards}")
    print(f"Your total is now {sum_player}")
    print("-"*30)

if sum_player > 21:
    print("You bust! Dealer wins.")
else:
    dealer_cards = random.randint(1, 11) , random.randint(1, 11)
    sum_dealer = sum(dealer_cards)
    print(f"Dealer's cards are {dealer_cards}")
    print(f"Dealer's total is {sum_dealer}")
    print("-"*30)

    if sum_dealer > 21 or sum_player > sum_dealer:
        print(f"You win! Your total: {sum_player}, Dealer's total: {sum_dealer}")
    elif sum_player < sum_dealer:
        print(f"You lose! Your total: {sum_player}, Dealer's total: {sum_dealer}")
    else:
        print(f"It's a tie! Your total: {sum_player}, Dealer's total: {sum_dealer}")

