import time

#Global Variables (or whatever they're called in Python)
Word = "computers rule"
Lives = 10
Guessed = '_________ ____'

#Game Introduction
print('''Time to hang a man!''')
#Pauses to add suspense to the game
time.sleep(2)
print('''I mean, play hangman...\n''')
time.sleep(2)
print("""I am thinking of two words.""")
time.sleep(2)
print('''You are allowed 10 mistakes.''')
time.sleep(2)
print('''Guess a letter and I will tell you if it is in one of the words''')
time.sleep(2)
print('''I am thinking of.\n''')
time.sleep(2)
print('''Every time you guess wrong, you lose a life.''')
time.sleep(2)
print('''When you are sure of which letter you would like to guess, press "Enter".''')

#Game Logic Starts
while True:
    Guess = input('''What is your guess?\n''')
    #If too many characters are pressed
    if len(Guess) > 1:
        print('''Only enter 1 character.''')
        continue
    #If a number is pressed
    try:
        Guess = int(Guess)
        print('''Only enter letters.''')
        continue
    #Input has been validated
    except:
        pass

    #If they guess correctly
    if Guess in Word:
        Guessed = list(Guessed)
        #Search the secret word for the guessed character
        for index in range(len(Word)):
            Letter = Word[index]
            #When you find the index of the guessed character
            if Letter == Guess:
                #store the correctly guessed characters so the user can view their progress
                Guessed[index] = Letter
        Guessed = ''.join(Guessed)
        #show the user their progress
        print(Guessed)
        #if the user won
        if Guessed == Word:
            time.sleep(2)
            print('''\nYou're right!\n''')
            time.sleep(1.5)
            print('''And you win!!!\n''')
            break
    #If they don't guess correctly
    else:
        Lives -= 1
        #If they have no lives left
        if Lives == 0:
            input('You Lose!!! Hahahahaha!!!')
            exit()
        #when they have lives remaining
        else:
            print('You have ' + str(Lives) + ' mistakes remaining, tread carefully...')
            time.sleep(1)
            print('''Try again.''')
#The game will let the user read the final messages instead of closing.
input('Press any key to exit.')
