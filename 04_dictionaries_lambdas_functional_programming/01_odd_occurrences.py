from collections import Counter

occurrence_list = [item.lower() for item in input().split()]
odd_occurrence = [key for key, value in Counter(occurrence_list).items() if value % 2 != 0]
print(', '.join(list(odd_occurrence)))
