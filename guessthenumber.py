import random

print("Welcome to 'Guess the Number'! The computer will select a random number between 1 and 100 and your job is to guess it.")
print("Give a number and the computer will tell you if you're close by telling you Higher or Lower.")

randSelection = random.randint(0, 100)
guess = False

while guess == False:
    numGuess = int(input("What's your guess?: "))
    if numGuess > randSelection:
        print("The computer says Lower!")
    elif  numGuess < randSelection:
        print("The computer says Higher!")
    else:
        guess = True
        
print(f"You have guessed correctly! The number was {randSelection}!")