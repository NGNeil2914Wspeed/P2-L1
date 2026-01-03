from time import sleep

condition = input("Please enter 'y' if the student has a condititon else enter 'n'")
if (condition == 'y'):
    condition = True
else:
    condition = False

if (condition == True):
    print ("Allowed")
else:
    total_students = input("How many students are there in total? ")
    if (total_students >= 75):
        print ("Allowed")
    else:
        print ("Not allowed")
