def print_sign(number):
    if number > 0:
        print("The number {0} is positive.".format(number))
    elif number < 0:
        print("The number {0} is negative.".format(number))
    else:
        print("The number {0} is zero.".format(number))


print_sign(int(input()))
