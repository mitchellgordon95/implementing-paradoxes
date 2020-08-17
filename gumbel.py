import numpy as np

def gumbel(size):
    u = np.random.uniform(size=size)
    return -np.log(-np.log(u))

probs = np.array([0.25, 0.6, 0.15])
log_probs = np.log(probs)

counts = np.zeros(probs.shape[0])
for i in range(100000):
    sample = np.argmax(gumbel(probs.shape[0]) + log_probs)
    counts[sample] += 1

for i in range(probs.shape[0]):
    print(f'{counts[i]} / {np.sum(counts)} = {counts[i] / np.sum(counts)}')

