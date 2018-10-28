import numpy as np


def sigmoid(x):
    return 1. / (1. + np.exp(-x))

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[3, 4], [5, 6], [7, 8]])
c = sigmoid(a)
d = c * (1 - c)




print("a = ")
print(a)
print("\nb = ")
print(b)
print("\nc = ")
print(c)
print("\nd = ")
print(d)

