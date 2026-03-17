import random
import guess_art
import os
import guess_data

logo=guess_art.logo
vs_logo=guess_art.vs_logo
celeb_data=guess_data.celebs_data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(choice_a,choice_b):
    if choice_a["followers"]>choice_b["followers"]:
        return 'A'
    else :
        return 'B'

def game(choice_a,choice_b,score):
    clear_screen()
    # print(choice_a)
    # print(choice_b)
    print(logo)
    if score!=0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {choice_a['name']} ,{choice_a['description']}")
    print(vs_logo)
    print(f"Compare B: {choice_b['name']} ,{choice_b['description']}")
    user_guess=input("Who has more followers? Type 'A' or 'B': ").upper()
    # print(compare(choice_a,choice_b))
    if user_guess==compare(choice_a,choice_b):
        score+=1        
        if user_guess=='B':
            choice_a=choice_b    
        choice_b=random.choice(celeb_data)
        while(choice_a==choice_b):
            choice_b=random.choice(celeb_data)
        game(choice_a,choice_b,score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

choice_a=random.choice(celeb_data)
choice_b=random.choice(celeb_data)
score=0
while(choice_a==choice_b):
    choice_b=random.choice(celeb_data)
game(choice_a,choice_b,score)