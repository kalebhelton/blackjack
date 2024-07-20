#name: kalebhelton
#started:  07/19/2024
#ended:
#blackjack

import random

# create card categories + values
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_lists = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in card_lists]
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
       return 11
    else:
        return int(card[0])
    
# create a function to shuffle the cards
# distribute 2 cards to the player + dealer 
random.shuffle(deck)
player_card = [deck.pop(), deck.pop()] #players first 2 cards
dealer_card1 = deck.pop() #card that shows to the player
dealer_card2 = deck.pop() #card revealed after the player has gone

while True:
    player_score = sum(card_value(card) for card in player_card)
    print("Player Has: ", player_card, " ", player_score)
    print("Dealer Has: ", dealer_card1)
    print("\n")

    choice = input('Would you like to hit or stay? ["hit" to request another card, "stay" to stop]: ').lower()
    if player_score < 21:
        if choice == "hit": 
            new_card = deck.pop() 
            player_card.append(new_card) 
        elif choice == "stay": 
            break
        else: 
            print("Invalid choice. Please try again.") 
            continue
    elif player_score == 21:
        print("Player has 21.")
        break
    else:
        print("Player has Busted.")
        break

dealer_cards = [dealer_card1, dealer_card2]
dealer_score = sum(card_value(card) for card in dealer_cards)
while dealer_score < 17:
    new_card = deck.pop()
    dealer_cards.append(new_card)
    dealer_score += card_value(new_card)

print("Dealer Has: ", dealer_cards, " ", dealer_score)
print("\n")

if dealer_score > 21:
    print("Dealer has Busted.")
    print("Winner = Player")

elif player_score > dealer_score:
    print("Dealer Has: ", dealer_cards, " ", dealer_score)
    print("Player Has: ", player_card, " ", player_score)
    print("Winner = Player")

elif dealer_score > player_score:
    print("Dealer Has: ", dealer_cards, " ", dealer_score)
    print("Player Has: ", player_card, " ", player_score)
    print("Winner = Dealer")

else:
    print("Dealer Has: ", dealer_cards, " ", dealer_score)
    print("Player Has: ", player_card, " ", player_score)
    print("Push")