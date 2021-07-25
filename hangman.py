  
# Importing Modules

import random
import sys
import time

'''-------------------------------------------------------------------------------------'''


def exit_game():
    print("Thank You for playing")
    sys.exit()


# Enter Passcode to Start Playing

print('You need a password before accessing the game.')
time.sleep(0.5)
try1 = 0

while True:
    if try1 == 3:
        time.sleep(1)
        print("Cheaters not allowed")
        sys.exit()
    s = input('''
Please enter the passcode below:
''')
    if s == 'exit':
        exit_game()

    try:
        val = int(s)
    except ValueError:
        print("Are you sure you entered a passcode?")
        time.sleep(1)
        try1 += 1
        print("You have", 3 - try1, "more chances left to try")
        time.sleep(1)
        continue
       
    if val == 1234:  # Password is 1234
        print('''
Welcome
''')
        break
    try1 += 1
    if try1 < 3:  # One can't enter more than 3 times
        print("Sorry! the passcode entered by you is wrong! Please Try Again!")
        time.sleep(0.5)
        print("You have", 3 - try1, "more chances left to try")
        continue

time.sleep(1)  # Wait before execute next command

'''----------------------------------------------------------------------------------'''

# Enter your name and game would greet you

name = input('''Hi! What is your name?
''')

while name == '':
    name = input("Please Enter Your Name: ")

time.sleep(0.5)

if name == 'exit':
    exit_game()

print('''
Welcome {}!
It's time to play Hangman!'''.format(name))


##########################################################################

def instructions():  # Instructions for new players
    print('''
Instructions:''')
    time.sleep(1)

    print('''This is Hangman! A great fun game.''')
    time.sleep(1.5)

    print('''
An innocent person has been caught and only you know that
he is innocent. You want to free him off.
''')
    time.sleep(4)

    print('''Your statement has been recorded and will be used 
as an evidence in his favour. At final You are told to
prove that your statement was told completely awake''')
    time.sleep(6)

    print('''
To prove this you have to guess a genuine word in given 
attempts''')
    time.sleep(1.5)

    while True:  # Only press enter to continue
        start1 = input("Press Enter to Continue...")
        if start1 == 'exit':
            exit_game()

        elif start1 not in '':
            print('Invalid Input')
            continue

        else:
            break

    print('''
At starting you will be given number of letters in your word
along with group of word belongs to.
''')
    time.sleep(3.5)

    print("You have to guess the word letter by letter")
    time.sleep(2)

    print('''
A correct letter would be inserted in your word''')
    time.sleep(2.5)

    print("A wrong letter would increase your guess counter")
    time.sleep(2.5)

    print("Once the guess counter becomes zero you lose")
    time.sleep(2)

    print('''
Try to find the word at maximum guess counter
''')
    time.sleep(2)

    print('''
(Type 'exit' (and press enter) anytime to exit playing

Repeated letters or invalid letters like @,$ will 
not increase your guess counter

Do not try to enter more than one letter at a time;
Only first letter would be acceptable in this case.

However, if you are sure that you got the word you can
enter the word to win otherwise above case would be applied.)
''')
    time.sleep(6)

    while True:
        start2 = input('''
Are You Ready?

Press Enter to Continue...''')

        if start2 == 'exit':
            exit_game()

        elif start2 not in '':
            print('Invalid Input')
            continue

        if start2 in '':
            break


time.sleep(1)

while True:  # This would ask for instructions
    know_the_game = input('''
Do you know how to play?
''').lower()

    if know_the_game == 'exit':
        exit_game()

    elif know_the_game not in ('yes', 'y', 'no', 'n'):
        print('Invalid Input!')
        continue

    if know_the_game in ('no', 'n'):
        instructions()
    break

time.sleep(0.5)

#################################################################

print('''
Great! Let's start
''')

time.sleep(1)

print('''
A code by Ahmed Hammami
''')
time.sleep(0.5)

print("-----------------------------------------------")
print()
time.sleep(1)

# Main Code Starts Here
ascii_letters = 'abcdefghijklmnopqrstuvwxyz'  # English alphabets
# List of words in game
fruits = ['apple', 'olive', 'tomato', 'melon', 'litchi',
          'mango', 'lime', 'kiwi', 'grapes', 'cherry',
          'banana', 'apricot', 'cucumber', 'guava', 'mulberry',
          'orange', 'papaya', 'pear', 'peach', 'berry']

animals = ['ants', 'hippo', 'panda', 'giraffe', 'bat', 'bear',
           'catfish', 'cheetah', 'lizard', 'wolf', 'zebra', 'eagle',
           'cobra', 'goose', 'penguin', 'frog', 'mouse', 'flamingo',
           'rabbit', 'crow', 'whale', 'lion', 'monkey', 'ostrich',
           'peacock', 'raccoon', 'rhinoceros', 'sheep', 'dogs',
           'squirrel', 'tiger', 'vulture']

accessories = ['ring', 'bangle', 'lipstick', 'handbag', 'crown',
               'necklace', 'watch', 'caps', 'glasses', 'wallet',
               'belts', 'comb', 'pendent', 'earring', 'scarf',
               'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
               'jacket', 'boots', 'socks', 'stocking', 'muffler',
               'gloves', 'umbrella', 'ribbon']

stationary = ['notebook', 'tape', 'pencil', 'eraser', 'sharpener',
              'files', 'fevicol', 'inkpot', 'chalk', 'duster',
              'glue', 'paper', 'cutter', 'chart', 'colours',
              'stapler', 'marker', 'staples', 'clips', 'calculator',
              'envelope', 'register']

list = fruits + animals + accessories + stationary

########################################################################

while True:
    word = random.choice(list)

    print("Your word has", len(word), "letters.")
    # Game would randomly choose words
    time.sleep(1)
    print()

    if word in fruits:  # Give category of word
        print("Your word is a Fruit.")
    elif word in accessories:
        print("Your word is related to Accessory.")
    elif word in stationary:
        print("Your word is related to Stationary.")
    elif word in animals:
        print("Your word is a Animal")

    time.sleep(1.5)

    turns = 11 - len(word)  # No of free chances of guess
    if len(word) >= 8:
        turns = 4

    print('''
You have {} free chances to guess your word
Otherwise an innocent would be hanged!!!
'''.format(turns))

    time.sleep(1.8)

    while True:  # Only Press Enter
        start = input("Press Enter to Start Guessing...")

        if start == 'exit':
            exit_game()

        elif start not in '':
            print('Invalid Input')
            continue

        else:
            break

    guesses = ''
    while turns > 0:  # ask till turns are left
        failed = 0

        guess = input('''
Guess a Character: ''').lower()

        def won():
            print('''
You won!''')
            time.sleep(0.5)

            print("The word was {}.".format(word))  # You win
            time.sleep(1.5)

            print('''
             /////
           ( . . )
            \ - /
              _
          _ -   - _
         / /     \ \.
        / /|     || |
     ()  / |     || |
     ( )/   ----- (_)
          /_  ||  _\.
           |  ||  |
           |  ||  |
         (___) (___)

An Innocent has been saved''')
        if guess == word:
            won()
            break
           
        elif guess == 'exit':  # Game will exit on typing exit
            exit_game()

        elif guess in '':  # Enter will not work here
            print('''
Please enter a valid character.
''')
            continue

        else:
            guess = guess[0]

        if guess in guesses:  # In case you re-enter a letter
            print("You've already guessed this Character.")
            continue

        guesses += guess

        for char in word:  # will enter letter in word
            if char in guesses:
                print(char, " ", end="")

            else:  # not be disclosed till not entered
                print("_ ", end="")
                failed += 1
        if failed == 0:
            won()
            break
        if guess in word:  # Tell if letter is in word
            print('''
Excellent! {} is in the word'''.format(guess))

        if guess not in word:
            if guess not in ascii_letters:  # only enter alphabets
                print('''
Please enter a valid character.
''')
            else:  # Tell if letter is not in word
                print('''

Wrong!
It seems that {} is not in the word
'''.format(guess))

                # Turns will also decrease if wrong
                turns -= 1

            if turns != 0:  # Tell no of turns left
                print("You have", turns, 'more guess(es) left')

            elif turns == 0:  # If no turns left you lose
                print("Grr! You have no more turns to guess")
                time.sleep(0.5)

                print("You Lose")
                time.sleep(1)

                print('''
The word was {}.'''.format(word))
                time.sleep(1.5)

                print('''     ^
    | |
    | |________________________
    | |________________________>
    | |           |
    | |           |
    | |           |
    | |          / \        
    | |        ( *_* )
    | |          \ /
    | |         -   -
    | |      ./ |   | \.
    | |      () |   | ()
    | |          ---
    | |         ( | )
    | |         | || |
    | |        (__||__)
    | |
    | |
    | |
------------
An innocent was hanged!!!''')

    time.sleep(1.8)

    ###########################################################

    while True:  # If you want to play again

        play_again = input('''
Do you want to play again?
''').lower()

        if play_again in ('y', 'n', 'yes', 'no'):
            break
        print('Invalid input.')

    if play_again in ('y', 'yes'):
        time.sleep(1.5)
        continue

    else:
        time.sleep(0.5)

        # Thank You message by creator of game
        print('''
Thank You For Playing!
                                    -Ahmed Hammami''')
        break
time.sleep(3)
