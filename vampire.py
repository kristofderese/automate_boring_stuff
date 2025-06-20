name = input("What is your name?  ")
age = int(input("What is your age, " + name + "? "))
if name == "Kristof":
        print("Hi, Kristof!")
elif age < 12:
    print("You are not Kristof, Kiddo")
elif age > 2000:
    print("Vampire!")
elif age > 100:
    print("Grannie")
