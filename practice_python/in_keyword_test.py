a = [2,2,3,4,5,5,6,6]
b = [1, 1, 2, 2, 3, 5, 5, 8, 13, 21, 34, 55, 89]
c = []

for a in b:
    if a in b:
        c.append(a)

print(c)
