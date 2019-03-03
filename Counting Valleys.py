# Counting Valleys

n = int(input())

s = input()

sea_level = 0

hike = 0

if n == len(s):

    for i in s:
        if i == 'U':
            sea_level = sea_level + 1
        if i == 'D':
            sea_level = sea_level - 1
        if sea_level == 0 and i == 'U':
            hike = hike + 1
    print(hike)
