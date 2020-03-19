import numpy as np

def matmul(A,B):
    assert A.shape[1] == B.shape[0]
    rows, middle, cols = A.shape[0], A.shape[1], B.shape[1]
    out = np.zeros((rows, cols))

    for row in range(rows):
        for col in range(cols):
            for mid in range(middle):
                out[row,col] += A[row,mid] * B[mid,col]

    return out


def matmul3(A,B,C):
    assert A.shape[1] == B.shape[0]
    assert B.shape[1] == C.shape[0]
    rows, middle1, middle2, cols = A.shape[0], A.shape[1], C.shape[0], C.shape[1]
    out = np.zeros((rows, cols))

    for row in range(rows):
        for col in range(cols):
            for mid2 in range(middle2):
                for mid1 in range(middle1):
                    out[row,col] += A[row, mid1] * B[mid1, mid2]* C[mid2,col]

    return out

def matmul3_AB_first(A,B,C):
    assert A.shape[1] == B.shape[0]
    assert B.shape[1] == C.shape[0]
    rows, middle1, middle2, cols = A.shape[0], A.shape[1], C.shape[0], C.shape[1]
    out = np.zeros((rows, cols))
    AB = np.zeros((rows,middle2))


    for row in range(rows):
        for mid2 in range(middle2):
            # By caching the results of the AB computation, we save middle1 ops every time
            # a cached value is used. Below, the cached value is used rows * cols * middle2 times.
            # So caching saves us (rows * cols * middle2 - 1) * middle1 ops total.
            for mid1 in range(middle1):
                AB[row,mid2] += A[row, mid1] * B[mid1, mid2]
            for col in range(cols):
                # Doing this in the outside the mid1 loop saves us middle1 - 1 ops every time we get here.
                # So total, we save rows * cols * (middle1 - 1) * middle2
                out[row,col] += AB[row,mid2] * C[mid2,col]

    return out

def matmul3_BC_first(A,B,C):
    assert A.shape[1] == B.shape[0]
    assert B.shape[1] == C.shape[0]
    rows, middle1, middle2, cols = A.shape[0], A.shape[1], C.shape[0], C.shape[1]
    out = np.zeros((rows, cols))
    BC = np.zeros((middle1,cols))

    for col in range(cols):
        for mid1 in range(middle1):
            for mid2 in range(middle2):
                BC[mid1,col] += B[mid1, mid2] * C[mid2, col]
            for row in range(rows):
                out[row,col] += A[row,mid1] * BC[mid1,col]

    return out


A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,5],[3,9],[-6,15]])
C = np.array([[1,2,3,5],[5,5,5,5]])

ABC = matmul(matmul(A,B),C)
print(ABC)
assert np.all(ABC == matmul3(A,B,C))
assert np.all(ABC == matmul3_AB_first(A,B,C))
assert np.all(ABC == matmul3_BC_first(A,B,C))
