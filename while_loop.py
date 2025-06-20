spam = 0
if spam < 5:
    print("Spaham")
    spam = spam +1

jos = 0
while jos < 5:
    print ("Johos")
    jos = jos +1

while True:
    name = input("Who are you?  ")
    if name != "Jos":
        continue
    print ("Helle Jos! What is the password?   ")
    pw = input("<<  ")
    if pw == "lol":
        break
print("Access granted!")

x = 0
for x in range(10):
    x = x + 1
    print(x)

i = 0
while i < 10:
    i = i + 1
    print(i)
    continue