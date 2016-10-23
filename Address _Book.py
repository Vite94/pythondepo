#Address Book creator
#Ask user for whether they are looking up a contact or if they're adding a new contact
import time
import sys
choice = input("Enter 'looking for a contact' to search for a contact or Enter 'New contact' to add a new contact. Enter 'Exit' to exit.\n").lower()
while choice not in ["looking for a contact", "new contact","exit"]:
    print("Input invalid, please enter a correct input.")
    choice = input("Enter 'looking for a contact' to search for a contact or Enter 'New contact' to add a new contact.  Enter 'Exit' to exit.\n").lower()
while choice in ["looking for a contact", "new contact","exit"]:
    #Create and open a text file named Contacts
    try:
        contact = open("Contacts.txt", "r+")
        contact.close()
    except:
        contact = open("Contacts.txt", "w")
        contact.close()
    finally:
        if choice == "exit":
            choice2 = input("Are you sure? This will exit the program\n").lower()
            while choice2 not in ["yes", "y", "no", "n"]:
                print("Invalid input")
                choice2 = input("Are you sure? This will exit the program (Enter yes or no)\n").lower()
            if choice2 in ["yes", "y"]:
                try:        
                    print("Thank you for using this program made by Vithushan Elangovan. Goodbye!")
                    print("Exiting program in 3 seconds...Press CTRL+C to interrupt exit")
                    time.sleep(1)
                    print("3...Press CTRL+C to interrupt exit")
                    time.sleep(1)
                    print("2...Press CTRL+C to interrupt exit")
                    time.sleep(1)
                    print("1...Press CTRL+C to interrupt exit")
                    time.sleep(1)
                    print("Exit complete")
                    contact.close()
                    sys.exit()
                    quit()
                except KeyboardInterrupt:
                    print("Keyboard interrupt received. Returning to main menu.")
                    time.sleep(2)
                    choice = input("Enter 'looking for a contact' to search for a contact or Enter 'New contact' to add a new contact. Enter 'Exit' twice to exit program.\n").lower()
            elif choice2 in ["no", "n"]:
                choice = input("Enter 'looking for a contact' to search for a contact or Enter 'New contact' to add a new contact. Enter 'Exit' twice to exit program.\n").lower()
        if choice == "new contact":
            contact = open("Contacts.txt", "a")
            fname = input("Please enter the first name:\n")
            fname = fname[0].upper() + fname[1:].lower()
            mname = input("Please enter any middle names:\n")
            lname = input("Please enter the last name:\n")
            lname = lname[0].upper() + lname[1:].lower()
            #combines names to a full name
            name = fname + " " + mname + " " + lname
            contact.write("\n-------------------------------------------")
            contact.write("\nName: " + name)
            #age
            age = input("Please enter the age of " + fname + ":\n")
            contact.write("\t  Age: " + age)
            #date of birth
            d_o_b = input("Please enter the date of birth of " + fname + " in the format ddmmyyyy:\n")
            #to ensure date of birth is in correct format
            while len(d_o_b)!=8:
                print("Please enter the date in the format required")
                d_o_b = input("Please enter the date of birth of " + fname + " in the format ddmmyyyy:\n")
            while int(d_o_b[2:4])>12:
                print("Please enter the date in the format required")
                d_o_b = input("Please enter the date of birth of " + fname + " in the format ddmmyyyy:\n")
            while int(d_o_b[0:2])>31:
                print("Please enter the date in the format required")
                d_o_b = input("Please enter the date of birth of " + fname + " in the format ddmmyyyy:\n")
            contact.write("\nD.O.B: " + d_o_b[0:2] + "-" + d_o_b[2:4] + "-" + d_o_b[4:])
            #home phone
            hphone = input("Please enter the home phone number of " + fname + ":\n")
            contact.write("\nHome Phone: " + hphone)
            #mobile phone
            mphone = input("Please enter the mobile phone number of " + fname + ":\n")
            contact.write("\t  Mobile Phone: " + mphone)
            #address
            h_no = input("Please enter the house number and/or house name of " + fname + ":\n")
            street = input("Please enter the street of " + fname + ":\n")
            town = input("Please enter the town or city where " + fname + " lives in:\n")
            county = input("Please enter the county or state where " + fname + "lives in:\n")
            country = input("Please enter the country of residence of " + fname + ":\n")
            zip_code = input("Please enter the zip/postal code of " + fname + ":\n")
            address = h_no + " " + street + "\n\t" + town + "\n\t" + county + "\n\t" + country + "\n\t" + zip_code
            contact.write("\nAddress:\n\t" + address)
            print("Your contact has been successfully added.")
            #To carry on to next command
            choice = input("Would you like to add a new contact? or would you like to look for a contact? Type in 'exit' to close the document\n").lower()
        elif choice == "looking for a contact":
            contact = open("Contacts.txt", "r")
            firname = input("Please enter the first name of the contact you are looking for:\n")
            lstname = input("Please enter the last name of the contact you are looking for:\n")
            searchlines = contact.readlines()
            found = False
            for i,line in enumerate(searchlines):
                if (firname[0].upper()+firname[1:].lower()) in searchlines[i] and (lstname[0].upper()+lstname[1:].lower()) in searchlines[i]:
                    for l in searchlines[i:i+10]:
                        print(l),
                    print("")
                    found = True
                    break
            if not found:
                print("Contact not found")
        contact.close()
        choice = input("Please type in 'New contact' to add a contact or 'looking for a contact' to search your address book (Enter exit to exit the program):\n").lower()
