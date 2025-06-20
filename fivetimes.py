import random, sys

print('Hello!')
for i in range(5):
    print('On this iteration i is set to: ' + str(i))
print('Goodbye')

total = 0
amount = input('Enter number you want to add up:  ')
for i in range (int(amount)):
    total = total + i
print("The number is: " + str(total))

for i in range(5):
    print(random.randint(1,10))

while True:
    print('Type "exit" to exit')
    response = input('< ')
    if response == 'exit':
        sys.exit()
    print("You typed: " + response)