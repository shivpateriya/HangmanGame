import os
import random
import logo
import word_list
clear = lambda: os.system('cls')





chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)
lives =6
print(logo.logo)
#test code
print(chosen_word)

display=[]
for _ in range(word_length):
    display+='_'
end_game = False
while not end_game:
    guess =input('Guess a letter')

    if guess in display:
        print(f"you have already guess the letter{guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
         display[position]=letter
    #remove life of man
    # if letter!=guess:
    if guess not in chosen_word:
        print(f"you guessed{guess},that in the word .you loose a life")
        lives -=1
        if lives ==0:
            end_game=True
            print('You loose')
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_game = True
        print("you win ")
    print(logo.stages[lives])
    clear()
