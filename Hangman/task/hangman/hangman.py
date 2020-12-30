# Write your code here
import random

# Show HANGMAN message
def showtitle():
    print('H A N G M A N')
    startplay()


def startplay():
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        startasking(winner)
    elif menu == 'exit':
        exit()
    else:
        startplay()


wordlist = ['python', 'java', 'kotlin', 'javascript']
winner = random.choice(wordlist)
current_guess = '-' * len(winner)
lives = 8
guessed_letters = []


def guessword():
    guess = input('Guess the word {}: '.format(current_guess))
    if guess == winner:
        print('You survived!')
    else:
        print('You lost!')


def letterinword(word, letter):
    return [i for i, ltr in enumerate(word) if ltr == letter]


def startasking(word):

    global lives
    global guessed_letters
    # print(lives)
    while lives > 0:
        if winner == current_guess:
            print("You guessed the word!")
            print("You survived!")
            break
        # print()
        positions, letter = guessletter(word)
        if letter == None:
            startasking(word)
            break
        if letter in guessed_letters:
            print("You've already guessed this letter")
        elif len(positions) == 0:
            print("That letter doesn't appear in the word")
            lives = lives - 1
        else:
            updateword(letter, positions)
        # print("You have {} attempts left".format(lives))
        guessed_letters.append(letter)

    if winner != current_guess:
        print("You lost!")


def updateword(letter, positions):
    global current_guess
    for i in positions:
        current_guess = current_guess[:i] + letter + current_guess[i + 1:]


# Function to start the guessing
def guessletter(word):
    print('\r\n{}'.format(current_guess))
    letter = input("Input a letter: ")

    if len(letter) != 1:
        print('You should input a single letter')
        return None, None
    elif not letter.islower():
        print('Please enter a lowercase English letter')
        return None, None
    else:
        positions = letterinword(word, letter)
        return positions, letter


# Start the program!
showtitle()

