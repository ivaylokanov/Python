import numpy as np
A = [
    [1, 1, 1],
    [0, 2, 5],
    [2, 5, -1]
]

x = [
    [5],
    [3],
    [-2]
]
def multiply(A, x):
    """Multiplies the matrix A by the column vector x"""
    assert len(A[0]) == len(x)
    result = [[0] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[i])):
            result[i][0] = result[i][0] + (A[i][j] * x[j][0])
    return result
print(multiply(A,x))

A = np.array(A)
x = np.array(x)

print(A*x)