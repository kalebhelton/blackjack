# name: kalebhelton
# started:  07/19/2024
# ended:  
# blackjack

import random
import over21
import split

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

counter = 0 # counter for number of times a player can split -> max = 3
player_cards = [player_card1, player_card2]
dealer_cards = [dealer_card1, dealer_card2]

# card values -> accounts for Aces being 11
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace': # 'Ace' high -> @ the start of the each hand
       return 11
    else:
        return int(card[0])
    
player_score = sum(card_value(card) for card in player_cards)
dealer_score = sum(card_value(card) for card in dealer_cards)

while True:
    print("Player Has: ", player_cards, " ", player_score)
    print("Dealer Has: ", dealer_card1)
    print("\n")

    if player_score == 21:
        print("BLACKJACK!")
        break

    elif dealer_card1 == 'Ace': # INSURANCE -> NEEDS TO BE COMPLETED
        choice = input('Would you like insurance? ["yes" or "no]: ')
        if choice == "yes":
            break
        elif choice == "no":
            break

    elif dealer_score == 21:
        print("Unfortunatly, the Dealer has Blackjack :( Try Again.)")
        break

    if 0 <= counter <= 3: # Should stop the 'Split' section from running infinitivly 
        if split.split(player_card1, player_card2) == True:
            choice = input('Would you like to split? ["yes" or "no"]: ').lower()
            if choice == "yes" and counter <= 3:
                counter += 1
                new_card1 = deck.pop()
                player_cards1 = [player_card1, new_card1]
                player_cards1_score = sum(card_value(card) for card in player_cards1)
                if split.split(player_card1, new_card1) == True and counter <=3:
                    choice = input('Would you like to split? ["yes" or "no"]: ').lower()
                    if choice == "yes" and counter <= 3:
                        counter += 1
                        new_card2 = deck.pop()
                        player_cards2 = [player_card1, new_card2]
                        player_cards2_score = sum(card_value(card) for card in player_cards2)
                        if split.split(player_card1, new_card2) == True and counter <=3:
                            choice = input('Would you like to split? ["yes" or "no"]: ').lower()
                            if choice == "yes" and counter <= 3:
                                counter += 1
                                new_card3 = deck.pop()
                                player_cards3 = [player_card1, new_card3]
                                player_cards3_score = sum(card_value(card) for card in player_cards3)
                                while over21.greater_than_21(player_cards3_score) == False:
                                    print("Player Has: ", player_cards3, " ", player_cards3_score)
                                    print("Dealer Has: ", dealer_card1)
                                    choice = input('Would you like to hit or stay?: ').lower()
                                    if choice == "hit":
                                        new_card = deck.pop()
                                        player_cards3.append(new_card)
                                        player_cards3_score += card_value(new_card)
                                    elif choice == "stay":
                                        break
                                    else:
                                        print("Invalid Choice.  Try Again.")
                                        continue
                                new_card4 = deck.pop()
                                player_cards2 = [new_card2, new_card4]
                                player_cards2_score = sum(card_value(card) for card in player_cards2)
                                while over21.greater_than_21(player_cards2_score) == False:
                                    print("Player Has: ", player_cards2, " ", player_cards2_score)
                                    print("Dealer Has: ", dealer_card1)
                                    choice = input('Would you like to hit or stay?: ').lower()
                                    if choice == 'hit':
                                        new_card = deck.pop()
                                        player_cards2.append(new_card)
                                        player_cards2_score += card_value(new_card)
                                    elif choice == 'stay':
                                        break
                                    else: 
                                        print("Invalid Choice. Try Again.")
                                        continue
                                new_card5 = deck.pop()
                                player_cards1 = [new_card1, new_card5]
                                player_cards1_score = sum(card_value(card) for card in player_cards1)
                                while over21.greater_than_21(player_cards1_score) == False:
                                    print("Player Has: ", player_cards1, " ", player_cards1_score)
                                    print("Dealer Has: ", dealer_card1)
                                    choice = input('Would you like to hit or stay?: ').lower()
                                    if choice == 'hit':
                                        new_card = deck.pop()
                                        player_cards1.append(new_card)
                                        player_cards1_score += card_value(new_card)
                                    elif choice == 'stay':
                                        break
                                    else:
                                        print("Invalid Choice. Try Again.")
                                        continue
                                new_card6 = deck.pop()
                                player_cards0 = [player_card2, new_card6]
                                player_cards0_score = sum(card_value(card) for card in player_cards0)
                                while over21.greater_than_21(player_cards0_score) == False:
                                    print("Player Has: ", player_cards0, " ", player_cards0_score)
                                    print("Dealer Has: ", dealer_card1)
                                    choice = input('Would you like to hit or stay?: ').lower()
                                    if choice == 'hit':
                                        new_card = deck.pop()
                                        player_cards0.append(new_card)
                                        player_cards0_score += card_value(new_card)
                                    elif choice == 'stay':
                                        break
                                    else:
                                        print("Invalid Choice. Try Again.")
                                        continue
                            elif choice == "no":
                                while over21.greater_than_21(player_cards2_score):
                                    choice = input('Would you like to hit or stay?: ').lower()
                                    if choice == "hit":
                                        new_card = deck.pop()
                                        player_cards2.append(new_card)
                                        player_cards2_score += card_value(new_card)
                                    elif choice == "stay":
                                        break
                                    else:
                                        print("Invalid Choice. Try Again.")
                                        continue
                        elif split.split(player_card1, new_card2) == False:
                            while over21.greater_than_21(player_card1, new_card2):
                                choice = input('Would you like to hit or stay?: ').lower()
                                if choice == "hit":
                                    new_card = deck.pop()
                                    player_cards2.append(new_card)
                                    player_cards2_score += card_value(new_card)
                                    print("Player Has: ", player_cards2, " ", player_cards2_score)
                                elif choice == "stay":
                                    break
                                else:
                                    print("Invalid Choice. Try Again.")
                                    continue
                    elif choice == "no":
                        while over21.greater_than_21(player_cards1_score):
                            choice = input ('Would you like to hit or stay?: ').lower()
                            if choice == "hit":
                                new_card = deck.pop()
                                player_cards1.append(new_card)
                                player_cards1_score += card_value(new_card)
                                print("Player Has: ", player_cards1, " ", player_cards1_score)
                            elif choice == "stay":
                                break
                            else:
                                print("Invalid Choice. Try Again.")
                                continue
                elif split.split(player_card1, new_card1) == False:
                    while over21.greater_than_21(player_cards1_score):
                        choice = input('Would you like to hit or stay?: ').lower()
                        if choice == "hit":
                            new_card = deck.pop()
                            player_cards1.append(new_card)
                            player_cards1_score += card_value(new_card)
                        elif choice == "stay":
                            break
                        else:
                            print("Invalid Choice. Try Again.")
                            continue
                elif choice == "no":
                    while over21.greater_than_21(player_cards1_score):
                        choice = input ('Would you like to hit or stay?: ').lower()
                        if choice == "hit":
                            new_card = deck.pop()
                            player_cards1.append(new_card)
                            player_cards1_score += card_value(new_card)
                            print("Player Has: ", player_cards1, " ", player_cards1_score)
                        elif choice == "stay":
                            break
                        else:
                            print("Invalid Choice. Try Again.")
                            continue
            elif choice == "no":
                while over21.greater_than_21(player_score) == False:
                    choice = input('Would you like to hit or stay? ').lower()
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
            else:
                continue
        else: # no split -> just original 2 cards dealt
            while over21.greater_than_21(player_score) == False:
                choice = input('Would you like to hit or stay? ').lower()
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

dealer_score = sum(card_value(card) for card in dealer_cards)
while dealer_score < 17 and player_score != 21 and over21.greater_than_21(player_score) == False and over21.greater_than_21(dealer_score) == False:
    new_card = deck.pop()
    dealer_cards.append(new_card)
    dealer_score += card_value(new_card)
    print("Dealer Has: ", dealer_cards, " ", dealer_score)
    print("\n")

while player_score <= 21 and dealer_score <=21:
    if player_score > dealer_score and player_score <= 21:
        print("Winner = Player")

    elif dealer_score > player_score:
        print("Winner = Dealer")

    elif dealer_score == player_score:
        print("Push")

    else:
        print("Dealer has Busted.")
        print("Winner = Player")