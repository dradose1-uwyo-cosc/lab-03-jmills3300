# JW Mills
# UWYO COSC 1010
# 9/29/2024
# Lab 03 
# Lab Section: 12
# Sources, people worked with, help given to: None


# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
print("\n")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
states = ["Wyoming", "Colorado", "Montana"]

#print the entire list
for state in states:
    print(state)


#now print the first element in the list
print(states[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(states[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{states[1]} is south of {states[0]}")
print("\n")




print("Part Two------------------------------------------------------------------------")
print("\n")
#Append the following states to your list: Washington, Oregon, California and print your list
states.append("Washington")
states.append("Oregon")
states.append("California")
for state in states:
    print(state)
print("\n")

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
states[-2] = ("Maine")
for state in states:
    print(state)
print("\n")

#Insert the state Texas to be the third element in the list, again printing your list
states.insert(2, "Texas")
for state in states:
    print(state)
print("\n")

#Using the `del` statement remove the fourth item from the list, print your list 
del states[3]
for state in states:
    print(state)
print("\n")

#Remove Texas using its value, print the list
states.remove('Texas')
for state in states:
    print(state)
print("\n")

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(states))
print(states)

#Permanently sort your list in reverse order, printing it out
states.sort(reverse = True)
print("\n")

#Using the reverse method reverse the list and print it
states.reverse()
for state in states:
    print(state)


