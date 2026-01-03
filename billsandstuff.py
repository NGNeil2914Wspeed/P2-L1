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
units = getint("please enter number of units", None, None)

if (units <= 50):
    amount = units * 2.60
    surcharge = 25
elif (units <= 100):
    amount = 130+((units-50)*3.25)
    supercharge = 35
elif (units <= 200):
    amount = 130+((units-100)*5.26)
    supercharge = 45
else:
    amount = 130+((units-200)*8.45)
    supercharge = 75

print (f"The bill is "{%(amount+supercharge)})