#!/usr/bin/python3
import math
import numpy as np

# Please do not change the below function name and parameters
def cal_percentile(values,k):
    values.sort()
    n = len(values)
    i = (k * n)/100
    j = math.ceil(i)
    if 1 <= j <= n:
        print(values[j - 1])
    elif j == 0:
        print(values[j])
    else: 
        print(-1)
    pass
cal_percentile([1, 4, 2, 20, 40, 45, 8, 0, 100, 9], 96)

