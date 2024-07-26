#name: kalebhelton
#started:  07/19/2024
#ended:
#blackjack

import random
import over21

# create card categories + values
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_lists = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in card_lists]
    
# create a function to shuffle the cards
# distribute 2 cards to the player + dealer 
random.shuffle(deck)
player_card1 = deck.pop() #player's 1st card
player_card2 = deck.pop() #player's 2nd card
dealer_card1 = deck.pop() #card that shows to the player
dealer_card2 = deck.pop() #card revealed after the player has gone

# card values -> accounts for Aces being 1 or 11
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
       if player_score >= 11 or dealer_score >= 11:
           return 1
       elif player_score < 11 or dealer_score < 11:
           return 11
    else:
        return int(card[0])

player_cards = [player_card1, player_card2]

while True:
    player_score = sum(card_value(card) for card in player_cards)
    print("Player Has: ", player_cards, " ", player_score)
    print("Dealer Has: ", dealer_card1)
    print("\n")

    if player_score == 21:
        print("BLACKJACK!")
        break

    elif card_value(player_card1) == card_value(player_card2):
        choice = input('Would you like to split? ["yes" or "no"]: ').lower()
        if choice == "yes":
            new_card = deck.pop()
            player_cards1 = [player_card1, new_card]
            player_cards1_score = sum(card_value(card) for card in player_cards1)
            while over21.greater_than_21(player_cards1_score) == False:
                print("Player Has: ", player_cards1, " ", player_cards1_score)
                print("Dealer Has: ", dealer_card1)
                choice = input('Would you like to hit or stay?').lower()
                if choice == "hit":
                    new_card = deck.pop()
                    player_cards1.append(new_card)
                    player_cards1_score += card_value(new_card)
                elif choice == "stay":
                    break
                else:
                    print("Invalid Choice.  Try Again.")
                    continue
            player_cards2 = [player_card2, new_card]
            player_cards2_score = sum(card_value(card) for card in player_cards2)
            while over21.greater_than_21(player_cards2_score) == False:    
                print("Player Has: ", player_cards2, " ", player_cards2_score)
                print("Dealer Has: ", dealer_card1)
                choice = input('Would you like to hit or stay?').lower()
                if choice == "hit":
                    new_card = deck.pop()
                    player_cards2.append(new_card)
                    player_cards2_score += card_value(new_card)
                elif choice == "stay":
                    break
                else:
                    print("Invalid Choice.  Try Again.")
                    continue

        elif choice == "no":
            while over21.greater_than_21(player_score) == False:
                print("Player Has: ", player_cards1, " ", player_cards1_score)
                print("Dealer Has: ", dealer_card1)
                choice = input('Would you like to hit or stay?').lower()
                if choice == "hit":
                    new_card = deck.pop()
                    player_cards.append(new_card)
                    player_score += card_value(new_card)
                    print("Player Has: ", player_cards, " ", player_score)
                elif choice == "stay":
                    break
                else:
                    print("Invalid Choice.  Try Again.")
                    continue
            
    elif over21.greater_than_21(player_score) == False:
        choice = input('Would you like to hit or stay?').lower()
        if choice == "hit":
            new_card = deck.pop()
            player_cards.append(new_card)
            player_score += card_value(new_card)
            print("Player Has: ", player_cards, " ", player_score)
        elif choice == "stay":
            break
        else:
            print("Invalid Choice.  Try Again.")
            continue

dealer_cards = [dealer_card1, dealer_card2]
dealer_score = sum(card_value(card) for card in dealer_cards)
while dealer_score < 17 and player_score != 21 and over21.greater_than_21(player_score) == False and greater_than_21(dealer_score) == False:
    new_card = deck.pop()
    dealer_cards.append(new_card)
    dealer_score += card_value(new_card)

print("Dealer Has: ", dealer_cards, " ", dealer_score)
print("\n")

while player_score <= 21 and dealer_score <=21:
    if player_score > dealer_score and player_score <= 21:
        print("Dealer Has: ", dealer_cards, " ", dealer_score)
        print("Player Has: ", player_cards, " ", player_score)
        print("Winner = Player")

    elif dealer_score > player_score:
        print("Dealer Has: ", dealer_cards, " ", dealer_score)
        print("Player Has: ", player_cards, " ", player_score)
        print("Winner = Dealer")

    elif dealer_score == player_score:
        print("Dealer Has: ", dealer_cards, " ", dealer_score)
        print("Player Has: ", player_cards, " ", player_score)
        print("Push")

    else:
        print("Dealer has Busted.")
        print("Winner = Player")