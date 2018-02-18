from collections import Counter
import collections

occurrence_list = input().split()
occurrence_list = map(float, occurrence_list)
counted_list = dict(sorted(Counter(occurrence_list).items()))
[print("{} -> {} times".format(float(key),value)) for (key, value) in counted_list.items()]
