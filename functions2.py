
import random

from logo import logo
from ascii import stages
from words import word_list
lives = 6
chosen_word = random.choice(word_list)
print(logo)
print(chosen_word)
word_length = len(chosen_word)
blanks = []
for x in chosen_word:
    blanks.append("_")
print(f'guess the word: {blanks}')
end_of_game = False
index = 0
while not end_of_game:
    guess = input("Choose a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            blanks[position] = letter

    print(blanks)
    if "_" not in blanks:
        end_of_game = True
        print("You win!")
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You loose!")
