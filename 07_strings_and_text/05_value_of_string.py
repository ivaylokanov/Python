text = input()
manipulated_text = text
type_of_case = input()
if type_of_case == "LOWERCASE":
    manipulated_text = text
    sum_of_value = sum([ord(ch) for ch in manipulated_text if ch.isalpha() and ch == ch.lower()])
if type_of_case == "UPPERCASE":
    manipulated_text = text
    sum_of_value = sum([ord(ch) for ch in manipulated_text if ch.isalpha() and ch == ch.upper()])
print(f'The total sum is: {sum_of_value}')