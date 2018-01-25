number = int(input())
number_abs = abs(number)
list_of_strings = list(str(number_abs))
list_of_digit = list(map(int, list_of_strings))


def digit_is_even(list_of_digit):
    even_list = []
    for i in list_of_digit:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def digit_is_odd(list_of_digit):
    odd_list = []
    for i in list_of_digit:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


multiply_sum = sum(digit_is_even(list_of_digit)) * sum(digit_is_odd(list_of_digit))
print(multiply_sum)
