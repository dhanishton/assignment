


contacts = { }

def menu():
    print("--------------------MENU----------------------")
    print("press 0 to look up an existing number.")
    print("press 1 to add a Person to the contact book.")
    print("press 2 to print all contacts")
    print("press 3 to delete an existing number")
    print("press 4 if you want to terminate program.")
    
    print("press any number from 6-9 to display Menu")
    print("----------------------------------------------")
    print("           DIGITAL CONTACT BOOK              ")
menu()
def display():
    for key, value1 in contacts.items():
        print(key, ":", value1)

def checkAlreadyExist(number,email):
    for value1 in contacts.values():
        if number in value1:
            return 1
        if email in value1:
            return 2    
    return 0

def displayLast():
    lastPerson=list(contacts.values())[len(contacts)-1]
    lastkey=list(contacts.keys())[len(contacts)-1]
    print(lastkey, ":",lastPerson)

def displayLastUpdatedPerson(name):
    lastPerson=contacts.get(name)
    print(name, ":",lastPerson)    
while True:

    try:
        choice = int(input("Enter command:"))
        
        if choice == 0:
            look = input("Name of number owner:").upper()
            keys = list(contacts.keys())
            values1 = list(contacts.values())

            print("Number of ", look, ":", values1[keys.index(look)])    
            
        elif choice == 1:
            Name = input("Name of new contact: ").upper()
            Number = input("Enter 10 digit number: ")
            Email = input("Enter your email:")
            if checkAlreadyExist(Number,Email)==1:
                print("Number already exist")
            elif checkAlreadyExist(Number,Email)==2:
                print("Email already exist")  

            else  :
                if len(Number) == 10:
                    #contacts.update({Name:[Number, "Mobile"]})
                    contacts.update({Name:["Number",Number,"Email",Email]})
                    print("              CONTACTS")
                    displayLastUpdatedPerson(Name)

                else:
                    print("Number is invalid.Please try again.")

       
        elif choice == 3:
            delete = input("Name of contact to remove:").upper()
            del contacts[delete]
            print("              CONTACTS")
            display()
        elif choice == 4:
            print("Thank you for using the Digital Contact Book!")
            break
        elif choice == 2:
            print("              CONTACTS")
            display()
        else:
            menu()
    except Exception as e:
        print(e)
        print(e.with_traceback)
        print("Invalid Command") 
        print(e.with_traceback)   
    

    