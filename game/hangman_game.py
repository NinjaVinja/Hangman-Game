import random
from hangman_words import words_list
from hangman_art import HANGMANPICS
from hangman_logo import logo,game_over_logo,win

print(logo)
lives = 6
chosen_word = random.choice(words_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("word to guess: " + placeholder)
game_over = False
correct_letters = []

while not game_over:
    print(f"**********{lives}/6 LIVES LEFT**********")
    guess = input("Guess a Letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guess {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else: 
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("********** It was: ",f"{chosen_word}You Lose**********!")
            print(game_over_logo)

    if "_" not in display:
        game_over = True
        print("**********You Win**********")
        print(win)
    
    print(HANGMANPICS[6 - lives])
