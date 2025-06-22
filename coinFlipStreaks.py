#FUD
#generate a list of 100 randomly selected "H" or "T"
#check if the list contains a streaks of 6 heads or 6 tails
#repeat 10000 times and calculate percentage of what runs contains a streak
# hint: random.randint(0, 1) will have 50% change to return 0 and 1

import random

def create_list():
    list_words = []
    for i in range(100):
        number = random.randint(0, 1)
        if number == 0:
            random_result = "H"
            list_words.append(random_result)
        else:
            random_result = "T"
            list_words.append(random_result)
    return list_words

def streak_check(some_list):
    # 'i' moet hier een integer index zijn, geen element uit de lijst
    for i in range(len(some_list) - 5): # Loop over de indexen
        current_slice = some_list[i : i + 6]
        if current_slice == ['H','H','H','H','H','H'] or \
           current_slice == ['T','T','T','T','T','T']:
            return True
    return False

count = 0
for x in range(10000):
    list_to_check = create_list()
    if streak_check(list_to_check):
        count = count + 1

percentage = (count / 10000) * 100
print(f'Een reeks bevat een streak {percentage:.2f}% van de tijd.')



