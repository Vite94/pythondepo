import random
name = input("Who is using the dice roller today?  \n")
limit = int(input("How many sides do you want your dice to have?  \n"))
choice = input("Would you like to roll the dice? Y/N  \n").lower()
while choice not in ["y","n","yes","no"]:
    print("Incorrect entry, please try again")
    choice = input("Would you like to roll the dice? Y/N  \n").lower()
while choice in ["y", "yes"]:
    print(random.randint(1,limit))
    choice = input("Would you like to roll again? Y/N  \n").lower()
    while choice not in ["y","n","yes","no"]:
        print("Incorrect entry, please try again")
        choice = input("Would you like to roll again? Y/N  \n").lower()
print("Thank you for using this dice roller, Good bye " + name)


