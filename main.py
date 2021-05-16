import random
import hangman_stages
import words_list
from replit import clear 

lives = 6
the_word = random.choice(words_list.words_list)
no_of_blanks = len(the_word)

print(hangman_stages.logo)

display_word = []
for i in range(0,no_of_blanks):
    display_word.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    
    if guess in display_word:
        print(f"You've already guessed {guess}")

    for position in range(no_of_blanks):
        if  the_word[position] == guess:
            display_word[position] = guess
    
    if not guess in the_word:
        print(f"You guessed {guess}, That's not in the word. You lose a life")
        lives -= 1 
        if lives == 0:
            end_of_game = True
            print("Game over!")
    
    print(f"{' '.join(display_word)}")
                
    if "_" not in display_word:
        end_of_game = True
        print("You win!")

    print(hangman_stages.stages[lives])
