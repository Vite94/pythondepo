#String Concatenator
print("Funky String Concatenator")
import random
name = input("What are you called?\n")
choice = input("Would you like to start concatenating random sentences?! Y/N \n").lower()
start = ["You are ", "I am ", "It is ", "We are ", "That is ", "They are ", "What is "]
mid = [" doing "," feeling "," changing "," running "," breaking "," playing "," singing "," crying "]
end = ["great.","well.","awesome.","up.","down.","sick."]
def concatenate(str):
    return str[random.randint(1, len(str)-1)]
while choice not in ["y", "yes", "n", "no"]:
    print("Please enter a valid answer\n")
    choice = input("Would you like to start concatenating random sentences?! Y/N \n").lower()
while choice in ["y","yes"]:
    print(concatenate(start) + concatenate(mid) + concatenate(end) + "\n")
    choice = input("Would you like to concatenate more sentences?! Y/N \n").lower()
    while choice not in ["y", "yes", "n", "no"]:
        print("Please enter a valid answer\n")
        choice = input("Would you like to concatenate more sentences?! Y/N \n").lower()
print("Thank you for using my string concatenator, goodbye " + name[0].upper() + name[1:].lower())

