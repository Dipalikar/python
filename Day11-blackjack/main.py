import random
import os
import blackjack_art

logo=blackjack_art.blackjack_logo
card_graphics=blackjack_art.card_graphics

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of a list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents a Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """Compares user and computer scores and returns the result"""
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:        
        return "Lose, opponent has a Blackjack!"
    elif user_score == 0:       
        return "Win with a Blackjack!"
    elif user_score > 21:        
        return "You went over. You lose!"
    elif computer_score > 21:        
        return "Opponent went over. You win!"
    elif user_score > computer_score:       
        return "You win!"
    else:       
        return "You lose!"
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_cards(cards):
    for card in cards:
        print(card_graphics.get(card, card))

def game(): 
    for i in range(2):
            User_cards.append(deal_card())
            Computer_cards.append(deal_card())
        
    user_score=calculate_score(User_cards)
    computer_score=calculate_score(Computer_cards)

    print("Your cards:")
    display_cards(User_cards)
    print(f"Score: {user_score}")
    print(f"Computer's first card is {Computer_cards[0]}")  

    if user_score == 0 or computer_score == 0:
     print(compare(user_score, computer_score))
     return
    
    
    while input("Type 'y' to get another card, type 'n' to pass: ").lower()=='y' :
        User_cards.append(deal_card())
        user_score=calculate_score(User_cards)

        print("Your cards:")
        display_cards(User_cards)
        print(f"Score: {user_score}")
        print(f"Computer's first hand is {computer_score}") 

        if user_score==0:         
         print("Win with a Blackjack!")
         return

        elif user_score > 21:
          print("You went over. You lose!")
          return
    
    while computer_score<17:
     Computer_cards.append(deal_card())
     computer_score=calculate_score(Computer_cards)
    
    print(compare(user_score,computer_score))    
  
    print(f"Your cards: {User_cards},current score is {user_score}")
    print(f"Computer's final hand is {Computer_cards} with score {computer_score}") 
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()=='y':
    clear_screen()
    print(logo)
    User_cards=[]
    Computer_cards=[]    
    game()

