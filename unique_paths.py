def fact(x):
    partial = 1
    for i in range(x):
        partial = partial * (i+1)

    return partial

def choose_fact(n, k):
    return fact(n) / fact(n - k) / fact(k)

def choose_recursive(n, k):
    if n == k:
        return 1
    if k == 0:
        return 1

    return choose_recursive(n-1, k) + choose_recursive(n-1, k-1)

def unique_paths(n, m):
    return choose_fact(n+m-2, n-1)


def unique_paths_decisions(n, m):
    # Returns the number of completed decisions at step x
    def decide(x, continuable):
        possible = continuable * 2
        decided = 0
        # We could compute these factorials faster by caching some stuff and being clever
        # But this approach is stricly worse than the row method, which takes min(n, m) iterations
        # It's more of a conceptual novelty
        if x >= n-1:
            decided += choose_fact(x-1, n-2)
        if x >= m-1:
            decided += choose_fact(x-1, m-2)

        return decided, possible - decided

    total = 0
    continuable = 1
    for step in range(1, n + m - 2):
        decided, continuable = decide(step, continuable)
        total += decided

    return total

print(unique_paths(7,25))
print(unique_paths_decisions(7,25))

# This view leads us to a very interesting way of computing a Pascal triangle number
def choose_double_hockey_stick(n, k):
    part1 = sum([choose_fact(i,i-1) for i in range(1,n-k+1)])
    part2 = sum([choose_fact(j,k) for j in range(k,n-k+1)])
    return part1 + part2

print(choose_fact(5,2))
print(choose_double_hockey_stick(5,2))


# And some other ways of getting a Pascal triangle number

def choose_staggered(n, k):
    L = 1
    cur_n = n-k
    # Start at n-k choose 1, stagger right and diag left to n-1 choose k-1
    for cur_k in range(1, k):
        # cur_n choose cur_k
        L_right = L * (cur_n - cur_k + 1) / cur_k
        # n-k+cur_k choose cur_k
        L = L + L_right
        cur_n += 1

    # Start at k choose k, stagger left and diag right to n-1 choose k
    R = 1
    for cur_n in range(k, n-1):
        # cur_n choose k - 1
        R_left = R * k / (cur_n - k + 1)
        # cur_n + 1 choose k
        R = R + R_left

    return L + R

# From https://medium.com/@duhroach/fast-fun-with-pascals-triangle-6030e15dced0
def pascalIndexInRowFast(row, index):
    lastVal=1
    halfRow = (row >> 1)

    #early out, is index < half? if so, compute to that instead
    if index > halfRow:
        index = halfRow - (halfRow - index)

    for i in range(0, index):
        lastVal = lastVal * (row - i) / (i + 1)

    return lastVal

import time

start = time.time()
pascalIndexInRowFast(131072,65563)
end = time.time()
print(end - start)

start = time.time()
# Oh lol my solution is completely superfluous. Just come at it from the either side, instead of doing both.
# Learn how to count, dummy.
choose_staggered(131072,65563)
end = time.time()
print(end - start)
