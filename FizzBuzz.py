#This program counts how many multiples of 2 numbers are in the limit you set
#Turns input into int form and defines limit as a string storing an int
limit = int(input("What limit would you like to set the count to? "))
multiple1 = int(input("What is the first multiple? "))
multiple2 = int(input("What is the second multiple? "))
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
print("Please type in exit() or break or simply close to exit")

