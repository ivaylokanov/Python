def print_line(start, end):
    for i in range(start, end + 1):
        print(i, end=" ")
    print()


def print_triangle(n):
    for i in range(n):
        print_line(1, i)
    for i in range(n, 0, -1):
        print_line(1, i)


print_triangle(int(input()))
