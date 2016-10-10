from random import randint
#Introductory Message
print("Welcome to Guess the number by Vithushan Elangovan \nGuess a number between 1 and 100")
#name of user
name = input("Who is playing today? \n")
#starts off play
play = input("Would you like to start the game? Y/N\n").lower()
while play not in ["y","n","yes","no"]:
    print("Incorrect input, please try again")
    play = input("Would you like to start the game? Y/N\n").lower()
while play in ["y","yes"]:
    #Randomly generated number
    num = randint(1, 100)
    #user guess
    guess = int(input("What do you think the number is " + name + "?\n"))
    #checks for correct input for integer between 1 and 100
    while guess not in range(1,101):
        print("Please enter an integer between 1 and 100")
    if abs(guess-num)<10:
        print("So close! The number was " + str(num) + "!")
    elif guess>num and (20>(guess-num)>10):
        print("That is too high! The number was " + str(num) + "!")
    elif guess<num and (20>num-guess>10):
        print("That is too low! The number was " + str(num) + "!")
    elif abs(guess-num)>20:
        print("That was nowhere near the number! The number was " + str(num) + "!")
    elif num == guess:
        print("That is amazing! You got it spot on " + name + "!")
    play = input("Would you like to play again? Y/N\n").lower()
print("Thank you for playing this game " + name + "!")
    
