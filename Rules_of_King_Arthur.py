#Battle Rules
print("You are a leader of one of King Arthur's search parties and are on the lookout for enemies. You must also follow the battle rules set by King Arthur himself.")
num_knights = int(input("Enter the number of knights you have available "))
day = input("Enter the day of the week ")
enemy = input("Enter the type of enemy you encounter ").lower()

if enemy == "killer bunny":
    print("Holy Hand Grenade!")
else:
    #Original Battle Rules
    if num_knights < 3 or day == "Monday":
        print("Retreat!")
    elif num_knights >= 10 and day == "Wednesday":
        print("Release the Trojan Rabbit!")
    else:
        print("Offer Truce?")
