#1
# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names) 

# => [6306819796133686941, 8135353348168144921, -1228887169324443034]

# names = ['Sam', 'Don', 'Daniel']
# names = map(lambda i:hash(i), names)
# print(list(names))

# names = ['Sam', 'Don', 'Daniel']
# names = map(hash, names)
# print(list(names))

# #2
# colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow" ]
# def is_red():
#     if a == "red":
#         return colors
# filter(is_red, a)

# colors_list = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow" ]
# sort_red = list(filter(lambda x: x == "red", colors_list))
# print(sort_red)

#3
# sps = ['1','2','3','4','5','7']
# new_sps = []
# for item in sps:
#     new_sps.append(int(item))
#     print (new_sps)

# sps = ['1','2','3','4','5','7']
# new_sps = list(map(int, sps))
# print (new_sps)

#4
# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(lambda x: round(x*1.6,2), mile_distances))
# print (kilometer_distances)

# def miles_to_kilometers(num_miles):
#     return round(num_miles * 1.6,2)
# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(miles_to_kilometers, mile_distances))
# print (kilometer_distances)

#5
# from functools import reduce
# sps = [2, 5, 7, 8, 9, 45]
# def max_number (a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(reduce(max_number, sps, 0))


#6
from functools import reduce
people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
height_total = 0 
height_count = 0 
for person in people: 
    if 'height' in person: 
        height_total += person['height'] 
        height_count += 1 
print(height_total)