import numpy as np

def shapes(A,B):
    assert A.shape[1] == B.shape[0]
    return A.shape[0], A.shape[1], B.shape[1]

def dot_prods(A,B):
    rows, middle, cols = shapes(A,B)
    out = np.zeros((rows, cols))

    for row in range(rows):
        for col in range(cols):
            for mid in range(middle):
                out[row,col] += A[row,mid] * B[mid,col]

    return out

def col_times_scalar(col, scalar):
    out = np.zeros(col.shape[0])
    for i in range(col.shape[0]):
        out[i] = col[i] * scalar
    return out

def lin_combo_cols(A,B):
    rows, middle, cols = shapes(A,B)
    out = np.zeros((rows, cols))

    for col in range(cols):
        for mid in range(middle):
            out[:,col] += col_times_scalar(A[:,mid], B[mid,col])

    return out

def row_times_scalar(scalar, row):
    out = np.zeros(row.shape[0])
    for i in range(row.shape[0]):
        out[i] = row[i] * scalar
    return out

def lin_combo_rows(A,B):
    rows, middle, cols = shapes(A,B)
    out = np.zeros((rows, cols))

    for row in range(rows):
        for mid in range(middle):
            out[row,:] += row_times_scalar(A[row,mid], B[mid,:])

    return out

def col_times_row(col, row):
    out = np.zeros((col.shape[0], row.shape[0]))
    for i in range(col.shape[0]):
        for j in range(row.shape[0]):
            out[i,j] = col[i] * row[j]
    return out

def components(A,B):
    rows, middle, cols = shapes(A,B)
    out = np.zeros((rows, cols))

    for mid in range(middle):
        out += col_times_row(A[:,mid], B[mid,:])
        """
        for row in range(rows):
            for col in range(cols):
                out[row,col] += A[row,mid] * B[mid,col]
        """

    return out

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,5],[3,9],[-6,15]])
AB = np.matmul(A,B)
print(AB)
assert np.all(AB == dot_prods(A,B))
assert np.all(AB == lin_combo_cols(A,B))
assert np.all(AB == lin_combo_rows(A,B))
assert np.all(AB == components(A,B))
