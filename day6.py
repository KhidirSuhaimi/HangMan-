
import random
word_list = ["aardvark","baboon","camel"]
placeholder = ""

chosen_word = random.choice(word_list)

for letter in chosen_word:
    placeholder += "_"
print(placeholder)
display = ''
guessed_letters =[]
lives = 6
game_over = False

while not game_over:
    display = ''
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in guessed_letters:
        print("You have already chosen that letter dummy!")
    for letter in chosen_word:


        if letter == guess_letter:
            display += letter
            guessed_letters.append(letter)
        elif letter in guessed_letters:
            display += letter
        else:
            display += '_'


    print(display)

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"{guess_letter} is not in word, Dumbo you lose a life!")
        if lives == 0:
            game_over = True
            print("You lost!")


    if "_" not in display:
        game_over = True
        print("You Won!")

    if not game_over :
        if lives > 1:
            print(f"You have {lives} lives left!")
        else:
            print(f"You have {lives} life left!")







