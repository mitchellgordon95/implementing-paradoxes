import numpy as np

def uniform(matrix1, matrix2, sample_size):
    indices = np.random.choice(matrix1.shape[0], size=sample_size, replace=False)
    return matrix1[indices], matrix2[indices], indices


def coreset(matrix1, matrix2, sample_size):
    """Samples rows according to the coreset probability distribution. Re-weights the second matrix accordingly."""
    assert matrix1.shape[0] == matrix2.shape[0]
    norms1 = np.linalg.norm(matrix1, axis=1)
    norms2 = np.max(matrix2, axis=1)[0]
    unnormalized_probs = norms1 * norms2
    probs = unnormalized_probs / np.sum(unnormalized_probs)
    matrix2 = matrix2 / (sample_size * probs).reshape(-1,1)
    indices = np.random.choice(matrix1.shape[0], size=sample_size, p=probs, replace=True)
    return matrix1[indices], matrix2[indices], indices

def randmatmul(matrix1, matrix2, sample_size):
    """Samples rows according to the coreset probability distribution. Re-weights the second matrix accordingly."""
    assert matrix1.shape[0] == matrix2.shape[0]
    norms1 = np.linalg.norm(matrix1, axis=1)
    norms2 = np.linalg.norm(matrix2, axis=1)
    unnormalized_probs = norms1 * norms2
    probs = unnormalized_probs / np.sum(unnormalized_probs)
    matrix2 = matrix2 / (sample_size * probs).reshape(-1,1)
    indices = np.random.choice(matrix1.shape[0], size=sample_size, p=probs, replace=True)
    return matrix1[indices], matrix2[indices], indices


for sample_size in [64, 50, 40, 30, 20, 10]:

    uniform_diff = 0
    randmatmul_diff = 0
    coreset_diff = 0
    total_AB = 0
    trials = 100
    for _ in range(trials):
        A = np.random.rand(64, 512)
        B = np.random.rand(64, 512)
        total_AB += np.linalg.norm(A) * np.linalg.norm(B)
        Ap, Bp, _ = uniform(A,B,sample_size)
        uniform_diff += np.linalg.norm(np.matmul(A.T,B) - np.matmul(Ap.T,Bp))
        Ap, Bp, _ = randmatmul(A,B,sample_size)
        randmatmul_diff += np.linalg.norm(np.matmul(A.T,B) - np.matmul(Ap.T,Bp))
        Ap, Bp, _ = coreset(A,B,sample_size)
        coreset_diff += np.linalg.norm(np.matmul(A.T,B) - np.matmul(Ap.T,Bp))

    print(sample_size)
    print(uniform_diff / trials)
    print(randmatmul_diff / trials)
    print(coreset_diff / trials)
    print(0.1 * total_AB / trials)
    print()

