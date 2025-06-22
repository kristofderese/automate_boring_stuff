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
            random_result = "S"
            list_words.append(random_result)


