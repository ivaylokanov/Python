text = input()
char_holder = {}

for index, ch in enumerate(text):
    if ch not in char_holder:
        char_holder[ch] = []
        char_holder[ch].append(str(index))
    else:
        char_holder[ch].append(str(index))
for char, value in char_holder.items():
    str_indexes = '/'.join(value)
    print(f'{char}:{str_indexes}')