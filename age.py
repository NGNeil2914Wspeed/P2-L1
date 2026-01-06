def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")
                 
age = getint("Please enter your age: ")
if (age > 9 and age < 21):
    print ("Your age is between 10 and 20")
else:
    print ("You are below 10 or above 20")