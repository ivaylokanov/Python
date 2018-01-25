def print_external_line(n):
    print('-' * 2 * n)


def print_middle_line(n):

    for i in range(n-2):
        print('-', end='')
        print('\\/' * (n - 1), end='')
        print('-')


n = int(input())
print_external_line(n)
print_middle_line(n)
print_external_line(n)
