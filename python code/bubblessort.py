#!/usr/bin/python3
# Please do not change the below function name and parameters
def bubbleSort(values):
    i = 0
    for i in range(len(values)^2):
        i += 1
        for j in range(len(values) - 1):
            if values[j] > values[j+1]:
                values[j : j+2] = [values[j+1], values[j]]
        pass
    pass
    print(values)
    pass
bubbleSort([3,2,5,4, 20, -6, 0 , -100])

