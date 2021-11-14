
#!/usr/bin/python3
import math
import numpy as np

# Please do not change the below function name and parameters
def predict(h_output ,weights, activation):
    s = 0
    for x in range(len(h_output)):
         s = s + h_output[x] * weights[x]
    if activation == 'sigmoid':
        print(1/(1 + exp(-s)))
    elif activation == 'tanh':
        print((exp(s) - exp(-s))/(exp(s) + exp(-s)))
    elif activation == 'relu':
        print(max(0, s))
    else:
        print(max(.00001*s, s))
    pass

predict([1, 2, 5], [8, 9, 7], 'relu')