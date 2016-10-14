#This program counts how many multiples of 2 numbers are in the limit you set
print("This program calculates the amount of multiples within a certain range")
name = input("Who is using this program?\n")
choice = input("Would you like to begin? Y/N\n").lower()
#function for fizzing or buzzing depending on which multiple is being counted
def fizzbuzz(n):
        result = []
        #creates a list called 'result' and adds to it through an if/else statement
        for x in range(1, n+1):
            if x % multiple1 == 0 and x % multiple2 == 0:
                result.append("fizz buzz")
            elif x % multiple1 == 0:
                result.append('fizz')
            elif x % multiple2 == 0:
                result.append('buzz')
            else:
                result.append(str(x))
        return result
while choice not in ["y", "n", "yes", "no"]:
    print("Incorrect entry, please try again.")
    choice = input("Would you like to begin? Y/N\n").lower()
#Turns input into int form and defines limit as a string storing an int
while choice in ["y", "yes"]:
    limit = int(input("What limit would you like to set the count to? "))
    multiple1 = int(input("What is the first multiple? "))
    multiple2 = int(input("What is the second multiple? "))
    fizz_or_buzz = input("Would you like to count the number of multiples of %d, of %d or both? " % (multiple1, multiple2)).lower()
    from collections import Counter
    #if statement for calculating which multiple is needed to be counted
    if fizz_or_buzz in ['both']:
        counter = str(fizzbuzz(limit).count("fizz buzz"))
        print("The total number of multiples of both (within the set limit) are " + counter)
    elif fizz_or_buzz in ["%d" % (multiple1)]:
        counter = str(fizzbuzz(limit).count("fizz") + fizzbuzz(limit).count("fizz buzz"))
        print("The total number of multiples of " + str(multiple1) + " (within the set limit) are " + counter)
    elif fizz_or_buzz in ["%d" % (multiple2)]:
        counter = str(fizzbuzz(limit).count("fizz buzz") + fizzbuzz(limit).count("fizz buzz"))
        print("The total number of multiples of " + str(multiple2) + " (within the set limit) are " + counter)
    else:
        print("Sorry, there has been an error, please try again")
    choice = input("Continue with another set of numbers? Y/N\n").lower()
    while choice not in ["y", "n", "yes", "no"]:
        print("Incorrect entry, please try again.")
        choice = input("Continue with another set of numbers? Y/N\n").lower()
print("Thank you for using this program " + name[0].upper() + name[1:].lower(). + "Goodbye!")
