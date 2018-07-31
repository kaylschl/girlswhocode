# GUESS THE NUMBER:
import random

print("Welcome to the 'guess-the-number' game!")
print("In order to play, guess a number between 1 and 20")
print("I will give you hints to help you get the correct value!")
print("You will only have 3 tries, though, until a new game begins!")

#TODO: define function guess_the_number
def guess_the_number():

#TODO: use random.randint to get a number between 1 and 20
    number = random.randint(1, 20)
#TODO: ask user to input their guess
    guess = int(input("Enter your guess: "))
    #TODO: loop to keep giving the player three guesses until they've guessed correctly
    for trials in range(2):
        #TODO: give the player cues if the guess is not correct
        if guess > number:
            print("Guess lower")
        else:
            print("Guess higher")
        guess = int(input("Enter your guess: "))

            #TODO: let the player know if the guess is correct
    if guess == number:
        print("YOU GUESSED CORRECTLY!")
    else:
        print("The correct answer was {}".format(number))
guess_the_number()



import random
def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this number even or odd?")
    if ((computer_value%2) == 0) and (user_input == "even"):
        print("YA DID IT! YOU SO SMORT\n")
    elif ((computer_value%2) == 0) and (user_input == "odd"):
        print("You're wrong.\n")
    elif ((computer_value%2) != 0) and (user_input == "even"):
        print("You're wrong.\n")
    elif ((computer_value%2) != 0) and (user_input == "odd"):
        print("YA DID IT.\n")

evenorodd()
