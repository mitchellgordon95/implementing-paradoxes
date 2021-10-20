import numpy as np

# Suppose x, y, and z are unit vectors.
# If y and z are close (in terms of cosine sim), does that imply that x is the same distance from y as it is from z?

# In other words, suppose cos_sim(y,z) >= 1 - epsilon
# Does that imply that cos_sim(x,y) ~= cos_sim(x,z)?

# Kind of. Consider this: we can perturb y a bit to get z. But we could pick many directions to perturb y. Which one is the best/worst case?
# The worst case is when we perturb y *away from x*, along the plane defined by x and y. Then we're moving farther away from y and x *at the same time*. So the distance from x to z is greater than the distance from x to y. Similar logic applies when we perturb y towards x (then the distance from x to z is less than the distance from x to y).

# However, the best case is when we perturb y perpendicular to the plane defined by x and y. Then the distance between x and y and the distance between x and z increase at about the same rate.

# Interestingly (and perhaps crucially) *most* directions are perpendicular to the plane in higher dimensions. So in practice if x ~ y and y ~ z then x ~ z

dim = 100000
cosine_diffs = []
small_diffs = []
for i in range(100):
    x = np.random.rand(dim)
    x = x / np.linalg.norm(x)
    y = np.random.rand(dim)
    y = y / np.linalg.norm(y)
    z = y
    direction = np.random.uniform(-1, 1, dim) / 1000
    while np.dot(y,z) > 0.99:
        z = z + direction
        z = z / np.linalg.norm(z)
    small_diffs.append(1 - np.dot(y,z))
    cosine_diffs.append(np.abs(np.dot(x,y) - np.dot(x,z)))

print(np.array(small_diffs).mean())
print(np.array(cosine_diffs).mean())
