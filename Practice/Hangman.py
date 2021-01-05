#Hangman Game
#By MJK618

import random

def hangman():
    words = ["Python", "Bugs", "Code", "Computer", "PHP","Web","Internet"]
    random_number = random.randint(0, len(words))
    word = words[random_number].lower() #so as user can add irrespective of cases
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter => ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:  
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

name = input("\nEnter your name : ")
print("Hello " + str(name).title() + "Welcome to the Hangman game.\nI am thinking of a word and you have to guess the letters of it one by one.")
print("After each wrong guess the culprit will be hanged a step forward.Try to save him")
ch = ''
while ch != 'q':
    
    hangman()
    ch = input("Press enter to play again or press 'q' to quit. : ")
