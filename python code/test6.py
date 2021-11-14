
#!/usr/bin/python3

import numpy as np

# Please do not change the below function name and parameters
def abs_error(arr1,arr2):
    s = 0
    for x in range(len(arr1)):
        s = s + abs(arr1[x] - arr2[x])
    print(s/len(arr1))
    pass
abs_error([1, 2, 3], [0, 0, 0])

