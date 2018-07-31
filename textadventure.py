#
# number = 25
# tries = 0
# guess = int(input("What number is it?"))
# while tries < 3 and number != guess:
#     print(tries)
#     tries += 1
#     if number > guess:
#         guess = int(input("Guess higher: "))
#     else:
#         guess = int(input("Guess lower"))
# print("The number is {}".format(number))
#
# number = 25
# tries = 0
#
# guess = int(input("What number is it?"))
# for i in range(2):
#     tries += 1
#     if number > guess:
#         guess = int(input("Guess higher: "))
#     elif number < guess:
#         guess = int(input("Guess lower"))
# print("The number is {}".format(number))


# Update this text to match your story.
start = '''
You are a penguin in the middle of a forest. You spot a castle in the distance.
You can go towards the castle or further into the forest.
'''

print(start)
while(True):
    print("Type 'yes' to go to the castle or 'no' to go to the forest.") # Update to match your story.
    user_input = input()
    if user_input == "yes":
        print("You decide to go to the castle and you stumble across a knight.")
        print("Type 'yes' to talk to the knight or 'no' to go back to the forest.") # Update to match your story.
        user_input = input()
        if user_input == "yes":
            print("The knight greets you and invites you to explore the castle with him!")
        elif user_input == "no":
            print("You return to the forest to venture further on your journey")
        # Continue code to finish story.
    elif user_input == "no":
        print("You choose to venture further into the forest and you are attacked by bats!") # Update to match your story.
# type "Ctrl C" to quit game loop
