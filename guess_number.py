import random

print("I am thinking of a number between 1 and 20")
think_number = random.randint(1,20)
num_guess = 0
while True:
    num_guess = num_guess + 1
    user_input = int(input("Take a guess:  "))
    if user_input > think_number:
        print('Too high! Try again!')
    elif user_input < think_number:
        print('Too low! Try again!')
    else:
        print("Super! You got it in " + str(num_guess) + " times!")
        break
