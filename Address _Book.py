#Address Book creater
#Ask user for whether they are looking up a contact or if they're adding a new contact
choice = input("Enter 'looking for a contact' to search for a contact or Enter 'New contact' to add a new contact\n").lower()
while choice not in ["looking for a contact", "new contact","exit"]:
    print("Input invalid, please enter a correct input.")
    choice = input("Enter 'looking for a contact' to search for a contact or Enter 'New contact' to add a new contact\n").lower()
while choice in ["looking for a contact", "new contact","exit"]:
    #Create and open a text file named Contacts
    if choice == "exit":
        print("Thank you for using this program made by Vithushan Elangovan. Goodbye!")
        contact.close()
        break
    try:
        contact = open("Contacts.txt", "r+")
        contact.close()
    except:
        contact = open("Contacts.txt", "w")
        contact.close()
    finally:
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
            contact.write("\tAge: " + age)
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
            contact.write("\t\tMobile Phone: " + mphone)
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
            firname = input("Please enter the first name of the contact you are looking for (Case Sensitive):\n")
            lstname = input("Please enter the last name of the contact you are looking for (Case Sensitive):\n")
            '''choice2 = input("Are you also looking to edit said contact? Please enter 'yes' or 'no'\n").lower() 
            while choice2 not in ["yes","y","no","n"]:
                print("Invalid entry, please enter the correct inputs.")
                choice2 = input("Are you also looking to edit said contact? Please enter 'yes' or 'no'\n").lower()
            if choice2 in ["no","n"]:'''
            searchlines = contact.readlines()
            for i,line in enumerate(searchlines):
                if firname in searchlines[i] and lstname in searchlines[i]:
                    for l in searchlines[i:i+10]:
                        print(l),
                    print("")
            contact.close()
            choice = input("Please type in 'New contact' to add a contact or 'looking for a contact' to search your address book (Enter exit to exit the program):\n").lower()
            '''elif choice2 in ["yes","y"]:
                contact = open("Contacts.txt", "r+")
                choice3 = input("What would you like to replace?\n")
                choice4 = input("What would you like to input into " + choice3 + ":\n")
                searchlines = contact.readlines()
                for i, line in enumerate(searchlines):
                    if fname in line and lname in line:
                        for l in searchlines[i:i+10]:
                            searchlines2 = searchlines.replace(choice3, choice3 + ": " + choice4)
                            contact.write(searchlines2)
                            print(l)
                        print()
                            
                        choice = input("Please type in 'New contact' to add a contact or 'looking for a contact' to search your address book:\n").lower()
                    else:
                        print("Contact not found")
                        choice = input("Please type in 'New contact' to add a contact or 'looking for a contact' to search your address book: Enter 'exit' to close the file and exit the program.\n").lower()
                        if choice == exit:
                            contact.close()
                            print("Thank you for using this program made by Vithushan Elangovan. Goodbye!")
                            break
                        else:
                            continue'''
                        
                
                
            
    
