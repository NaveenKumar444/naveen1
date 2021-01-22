name = ['nav', 'nit', 'is', 'am']
print(name[-1])
print(name[1:4])
print(name[:3])

# exercise

nav = [5, 8, 87, 2, 56, 23, 11, 1]
x = nav[0]
for i in nav:
    if i > x:
        x = i
print(f"the largest number in the list is: {x}")

# 2Dlists
matrix = [
    [1, 2, 3,],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for i in row:
        print(i)

# list methods

god = [5, 6, 7, 8, 7, 5]
for i in god:
    on = god.count(i)
    if on > 1:
        god.remove(i)
print(god)
# 2nd method
jo = []
for i in god:
    if i not in jo:
        jo.append(i)
print(jo)






