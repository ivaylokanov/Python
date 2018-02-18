size = int(input())
star = '*'
star1 = '*'
for i in range(size-1):
    star1 = star1 + star
print(star1)
for row in range(size-2):
    space = ''
    for i in range(1, size-1):
        space = space + ' '
        star2 = star + space + star
    print(star2)
print(star1)
