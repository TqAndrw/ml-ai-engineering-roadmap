import numpy as np


# 1. Broadcasting
a = np.ones((3, 1))
b = np.array([10, 20, 30, 40])
c = a + b

print("Broadcasting:")
print("a:", a.shape)
print("b:", b.shape)
print("c:", c.shape)


# 2. Reshape + indexing
values = np.arange(1, 13)
matrix = values.reshape(3, 4)

print("\nReshape:")
print(matrix)
print("Row 2:", matrix[1])
print("Column 3:", matrix[:, 2])
print("Row 3, Column 4:", matrix[2, 3])


# 3. Fancy + boolean indexing
scores = np.array([55, 72, 88, 41, 95, 67])

print("\nIndexing:")
print(scores[[1, 2, 4]])
print(scores[scores >= 70])


# 4. Transpose
data = np.array([
    [1, 10, 100],
    [2, 20, 200],
])

print("\nTranspose:")
print(data.shape)
print(data.T)
print(data.T.shape)


# 5. Standardization using broadcasting
X = np.array([
    [1.0, 10.0],
    [2.0, 20.0],
    [3.0, 30.0],
])

mean = X.mean(axis=0)
std = X.std(axis=0)
Z = (X - mean) / std

print("\nStandardization:")
print("mean:", mean)
print("std:", std)
print("Z:")
print(Z)
print("Z mean:", Z.mean(axis=0))
print("Z std:", Z.std(axis=0))


# 6. Floating-point precision
x = 0.1 + 0.2

print("\nFloating-point:")
print(x)
print(x == 0.3)
print(np.isclose(x, 0.3))
