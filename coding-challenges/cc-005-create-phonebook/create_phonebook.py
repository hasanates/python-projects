
print(" Welcome to the phonebook application")

phoneDict = {}
while (True):
    a=int(input("1. Find phone number\n2. Insert a phone number\n3. Delete a person from the phonebook\n4. Terminate\nSelect operation on Phonebook App (1/2/3/4) :"))
    if (a==1):
        person=input("Insert the name of the person: ")
        try:
            print(phoneDict[person])
        except:
            print("{} is not found".format(person))
    elif (a==2):
        person = input("Insert the name of the person: ")
        number=int(input("Insert phone number: "))
        phoneDict[person] = number
        print("{} added to phonebook".format(person))
    elif (a==3):
        person=input("whom to delete from phonebook: ")
        del phoneDict[person]
        print("{} deleted from the phonebook ".format(person))

    else:
        print("app is terminated")
        break