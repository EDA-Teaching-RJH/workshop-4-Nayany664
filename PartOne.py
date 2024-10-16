#ask for a name in camel case and output in snake case
#snake case is like first_name and preferred_first_name (Underscore and lowercase)
#camel case is like FirstName and preferredFirstName (all together)

#expect the input is shown as 1 word eg NayanyMuhunnthan instead of Nayany Muhunnthan
def change_case(fullname):
    firstname = [fullname[0].lower()]
    for a in fullname[1:]:
        if a in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") or a in (" "): #if there is a capital letter or a blank gap
            firstname.append ("_") #put an underscore after it
            firstname.append(a.lower()) #make it lower case
        else :
             firstname.append(a)  #if not uppercase or a gap, just keep it the same

    return " ".join(firstname)      

fullname = input("What is you full name?")
print(change_case(fullname))

