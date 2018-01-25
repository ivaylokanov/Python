import numpy as np
import  pandas as pd

element = input().split()
multiplier = int(input())
elements_in_numbers = map(int, element)
[print(item * multiplier, end=' ') for item in elements_in_numbers]

#a = np.mean(2, 3 ,5)
#print(a)
