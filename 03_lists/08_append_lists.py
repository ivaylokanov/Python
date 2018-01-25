sequence = input()
tidy_sequence = sequence.replace(' ', '').split('|')
if '' in tidy_sequence:
    tidy_sequence.remove('')
[print(' '.join(item), end=' ') for item in reversed(tidy_sequence)]
