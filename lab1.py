import math

# Part 1
area = math.pi * 5 ** 2
print(area)

volume = 4/3 * math.pi * 3 ** 3
print(volume)

c = (3 ** 2) + (4 ** 2)
hypo = math.sqrt(c)
print(hypo)

# Part 2
first_name = "Canyon"
last_name = "Merfy"
full_name = first_name + last_name

name_length = len(full_name)
print(full_name)
print(name_length)
print(full_name.upper())
print(full_name.lower())

# Part 3
height_ft = 6.5 #feet
height_in = height_ft * 12
weight = 205
bmi = (weight / (height_in ** 2)) * 703
print(bmi)