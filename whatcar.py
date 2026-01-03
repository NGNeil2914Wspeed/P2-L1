from time import sleep

def getint(question, min, max):
    while True:
        try:
            a = int(input(question))
            if (min and max == None):
                pass
            elif (a >= min and a <=max):
                pass
            else:
                print (f"Please enter a number between {min} and {max}")
                continue
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

wheeler =  getint("Please enter which type of vehicle you are driving\n 1. Four wheeler\n 2. Three wheeler\n 3. Two wheeler", 1, 2)
if (wheeler == 1):
    type_of_wheeler = getint(f"please enter the type of four wheeler:\n 1. Sedan\n 2. sports car", 1, 2)
    if (type_of_wheeler == 1):
        print ("Lame!")
    else:
        print ("not bad")
elif (wheeler == 2):
    type_of_wheeler = "lame"
    print ("whtever")
else:
    type_of_wheeler = getint("Please enter the type of 2 wheeler:\n 1. Bike\n 2. Scooter", 1, 2)
    if (type_of_wheeler == 1):
        print ("not bad")
    else:
        print ("lame")