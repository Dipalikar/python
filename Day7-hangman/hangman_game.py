import random
import hangman_art
import hangman_word

word_list=hangman_word.word_list
stage=hangman_art.stages
logo=hangman_art.logo

selected_word=random.choice(word_list)
word_length=len(selected_word)

lives=6
print(selected_word)
print(word_list)

flag=False
correct_count=0
print(logo)
while lives >=0 :
    if word_length==correct_count:
        print("Successfully Guessed the correct word:"+selected_word)
        exit()
    print(stage[lives])
    if lives == 0:
            print("Game over")
            exit() 
    selected_alphabet=input("Please enter your guessed alphabet ")

    for alphabet in selected_word:
     if selected_alphabet==alphabet:
        flag=True
        correct_count+=1
        exit
    
    if flag == True:
        print("Great Guess")
        flag=False
    else :
        lives-=1
        print("Incorrect Guess")    
      




        
            
            
        



