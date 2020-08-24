import numpy as np

PRIZES_NO_SPLITS = np.array([.1, .15, .70, 8, 0, 0, 0, 0, 0, 0, .3, 10, 0, 0])
ODDS = np.array([44, 72, 344, 3934, 108396, 8536197, 3277899625, 1.8, 3, 14, 164, 4517, 355675, 136579151])

probs = 1 / ODDS
probs = probs / np.sum(probs)

expected = np.sum(probs * PRIZES_NO_SPLITS)
print(f'Expected value: {expected}')

variance = np.sum(probs * (PRIZES_NO_SPLITS - expected)**2)
print(f'Variance: {variance}')

tickets = 400 * 52
print(f'{expected * tickets}')
print(f'{variance * tickets}')
print(f'{(variance * tickets)**0.5}')
