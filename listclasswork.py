
#Task3 : input again print without duplicate, ask to delete or add if chosen then print
#Global variable declaration
oldList = []
dupliCa = []
#Function calling
def chungo():

    #How many number should be needs to input the name
    user = int(input("Enter  how many number?:_"))

    #Now here user can iterator what input value until will be on.
    for i in range(user):
        name = input("Enter the name:")
        #Here add the value in oldList how many name are input
        oldList.append(name)

    for i in oldList:
        #Here if there name in duplicate then not print but if not
        # duplicate then will be print in dupli list.
        if i not in dupliCa:
            dupliCa.append(i)

    #Print the all name how many input from user
    print("All name are:", str(oldList))

    # Print the name only without duplicate name in list
    print("Without duplicate name are:", str(dupliCa))

# This is a function calling method
chungo()

# Here declare that what we should do? add or remove name from list that option created
# here user can choose one option.

addRemove = input("What do you want? if add click[a] or if remove click [r] element?:_")


# If we choose add option then we enter into add direction wa
if addRemove == "a" or addRemove == "r":
    def myhero():
        # How many number should be needs to input the name just for unique print I made
        # this function
        user = int(input("Enter number how many times you want add names?:_"))

        # Now here user can iterator what input value until will be on.
        for i in range(user):
            name = input("Enter the name:")
            # Here add the value in oldList how many name are input
            oldList.append(name)

        for i in oldList:
            # Here if there name in duplicate then not print but if not duplicate
            # then will be print in dupli list.
            if i not in dupliCa:
                dupliCa.append(i)

        print("All name are:", oldList)
        # Print the name only without duplicate name in list
        print("Without duplicate name are:", str(dupliCa))
        print("Congratulation you are successful to add name in list")

    myhero()
    def myrepeate():

     lastName = input("Do you want to continue?")
     if lastName == "yes":
       input("What do you want? if add click[a] or if remove click [r] element?:_")
       myhero()
    myrepeate()
    for result in myrepeate():
        print(result)
else:
    print(dupliCa)
    # What and which value you want to remove from list you can choose the value
    rename = input("Which name do you want remove from above list?:_")

    #This is a condition if here input name already in list then sure it will be removed from list
    if rename in dupliCa:
        dupliCa.remove(rename)

        # Now here finally print the value after removing value will be show us and print here
        print("After removing name are:", dupliCa)
        print("Congratulation! your successful to remove the name from above list")
    else:
        print("Sorry! this name is not found in  above list so you can not remove this name")




















