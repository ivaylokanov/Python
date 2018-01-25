sequence = input()
tidy_sequence = sequence.split('|')
tidy_sequence.reverse()
tidy_sequence = [item.split() for item in tidy_sequence]
[print(' '.join(item), end=' ') for item in tidy_sequence]
