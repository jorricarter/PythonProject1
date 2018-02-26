import time


def main():
    # Global Variables (or whatever they're called in Python)
    words = "computers rule"
    guessed = '_________ ____'
    lives = 10

    # Game Introduction
    print('''Time to hang a man!''')
    # Pauses to add suspense to the game
    time.sleep(1)
    print('''I mean, play hangman...\n''')
    time.sleep(1)
    print("""I am thinking of two words.""")
    time.sleep(1)
    print('''You are allowed 10 mistakes.''')
    time.sleep(1)
    print('''Guess a letter and I will tell you if it is in one of the words I am thinking of.\n''')
    time.sleep(2)
    print('''Every time you guess wrong, you lose a life.''')
    time.sleep(1)
    print('''When you are sure of which letter you would like to guess, press "Enter".''')
    time.sleep(2)

    # Game Logic Starts
    while True:
        guess = input('''What is your guess?\n''').lower()
        # Method to verify input
        if not validate_input(guess):
            continue
        pass

        # If they guess correctly
        if guess in words:
            # method to update guessed letters
            guessed = update_guessed(guess, words, guessed)
            # show the user their progress
            print(guessed)
            # if the user won
            if guessed == words:
                time.sleep(2)
                print('''\nYou're right!\n''')
                time.sleep(1.5)
                print('''And you win!!!\n''')
                break
        # If they don't guess correctly
        else:
            lives -= 1
            # If they have no lives left
            if lives == 0:
                input('You Lose!!! Hahahahaha!!!')
                exit()
            # When they have lives remaining
            else:
                print('You have ' + str(lives) + ' mistakes remaining, tread carefully...')
                time.sleep(1)
                print('''Try again.''')
    # The game will let the user read the final messages instead of closing.
    input('Press any key to exit.')


def validate_input(guess):
    # If too many characters are pressed
    if len(guess) > 1:
        print('''Only enter 1 character.''')
        return False
    # If a number is pressed
    try:
        # This returns false if guess is an integer.
        # Convert back to a string to return in output.
        guess = str(int(guess))
        print(guess + ' is not a letter\n'
                      'Only enter letters.\n')
        return False
    # Input has been validated
    except ValueError:
        return True


def update_guessed(guess, words, guessed):
    characters = list(guessed)
    # Search the secret word for the guessed character
    for index in range(len(words)):
        letter = words[index]
        # When you find the index of the guessed character
        if letter == guess:
            # store the correctly guessed characters so the user can view their progress
            characters[index] = letter
    return ''.join(characters)


if __name__ == '__main__':
    main()