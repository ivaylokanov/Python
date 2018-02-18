from collections import Counter
import collections

occurrence_list = input()
counted_list = dict(Counter(occurrence_list).items())
[print("{} -> {}".format(key,value)) for (key, value) in counted_list.items()]
