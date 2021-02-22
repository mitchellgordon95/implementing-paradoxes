import numpy as np

# Number of black and white balls in urn 0
urn0 = np.array([25, 75])
urn0 = urn0 / np.sum(urn0)

# Number of black and white balls in urn 1
urn1 = np.array([1, 100])
urn1 = urn1 / np.sum(urn1)


# Blindly pick an urn
urn_choice = np.random.randint(2)
print(f'Choose Urn {urn_choice}')

# Ok, at this point we have an urn, but we do not know which one.
# We assume a prior distribution over which urn we chose as 50/50 (which we happen to know is the best we can assume in this case).
# We know the ground truth is either [1,0] or [0,1].
urn_probs = [0.5, 0.5]

trials = 20
for _ in range(trials):
    # Sample a ball from the urn
    ball = np.random.choice([0,1], p=[urn0, urn1][urn_choice])

    # Now, we can update our beliefs about which urn we chose.
    ball_prob = urn0[ball] * urn_probs[0] + urn1[ball] * urn_probs[1]
    urn0_prob = urn0[ball] * urn_probs[0] / ball_prob

    urn_probs = [urn0_prob, 1 - urn0_prob]

    print(ball)
    print(urn_probs)








