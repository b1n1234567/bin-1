# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
# height (cm)
X = np.array([[142, 150, 153, 158, 163, 165, 168, 171, 173, 175, 178, 180, 220]]).T
# weight (kg)
y = np.array([[ 48, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 100]]).T

# Visualize data 
# plt.plot(X, y, 'ro')
# plt.axis([120, 240, 40, 120])
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.show()


# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)
# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(140, 240, 2)
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(X, y, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line
plt.axis([140, 230, 40, 120])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
