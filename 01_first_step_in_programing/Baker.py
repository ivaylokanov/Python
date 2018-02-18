bakeQty = int(input())
bakeCapacity = int(input())
CurniEatOnHour = int(input())
GanioEatOnHour = int(input())
hours = int(input())

productivityOnHour = bakeCapacity-CurniEatOnHour-GanioEatOnHour
if productivityOnHour*hours>=bakeQty:
    print('YES')
else:
    print('NO-',"{:.0f}".format(bakeQty-productivityOnHour*hours))
