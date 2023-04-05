from collections import Counter

# roll = (2, 1, 5, 4, 3, 4)

# roll = {4: 2, 5: 1, 3: 1, 2: 1, 1: 1}

# The keys are the sides of the dice, and the values are the occurances
# roll_2 = {3: 3, 5: 2, 6: 1}

roll_2 = (3, 3, 3, 5, 6, 5)

roll_dict = {}
for number in roll_2:
    if number in roll_dict:
        roll_dict[number] += 1
    else:
        roll_dict[number] = 1

# print(roll_2)
# print(roll_dict)
# print([0, 0, 3, 0, 2, 1])
# print()


# print(Counter((3, 3, 3, 5, 6, 5)).most_common())
# print(Counter((3, 3, 3, 5, 6, 5)).most_common(1))
# print(Counter((3, 3, 3, 5, 6, 5)).items())
# print(Counter((3, 3, 3, 5, 6, 5)).values())
roll = (3, 3, 3, 5, 6, 5)
roll = Counter(roll)
print(roll)
print(len(roll))
print(len(roll.most_common()))


