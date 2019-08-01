import math
# Let A be the set of all rationals whose square is less than 2.
# A = {p : p^2 < 2}

# A is unbounded above. For any rational p in A, we can construct another
# rational q which is also in A and greater than p.

n = 7
m = 5
assert n**2 / m**2 < 2
print(n / m)

for _ in range(10):
    # Keep multiplying the numerator and denominator by a common multiple.
    # Eventually, the denominator will be big enough that we can increase the
    # numerator without pushing the square past 2.
    mult = 2
    # Avoid floating point logic.
    # Equivalently: ((n * mult + 1) / (m * mult))**2 > 2
    # This loop must terminate. [^1]
    while (n * mult + 1)**2 > 2 * (m * mult)**2:
        mult += 1

    n_p = n * mult + 1
    m_p = m * mult

    # Using gte / lte here because we overflow floats very quickly
    assert n_p / m_p >= n / m
    assert n_p**2/m_p**2 <= 2

    n, m = n_p, m_p
    print(f'{n}/{m} = {n/m}')

print(math.sqrt(2))


# [^1] The while-loop will terminate when the left-hand side of the condition
# is greater than the right-hand side
def loop_terminates_when(n, m, mult):
    (n * mult + 1)**2 < 2 * (m * mult)**2


# We can re-write this condition as a polynomial of mult
def loop_terminates_when(n, m, mult):
    # Note: I used to have some algebra checking in here, but I deleted it for
    # brevity.
    return (2 * m**2 - n**2) * mult**2 - 2*n*mult - 1 > 0


# The first term of the polynomial will dominate its value, if mult becomes
# large enough. So if the first coefficient is positive, the left-side will
# eventually be positive. We won't prove this here.

# If you're willing to use calculus, you could say that the left side will
# eventually become positive if its second derivative is always positive.

# Therefore, the loop will terminate if the the square of our rational number
# is less than 2.
def loop_will_terminate(n, m):
    return 2 * m**2 - n**2 > 0
    # 2 * m**2 > n**2
    # (n/m)**2 < 2


# So the loop will terminate at least the first time it is run, because the
# square of the rational is less than 2.
n, m = 7, 5
assert loop_will_terminate(n, m)

# When the loop terminates, we have as the terminating condition:
mult = 15
assert 2 * (m * mult)**2 > (n * mult + 1)**2

# And then we substitute in our new values for n and m.
n = n * mult + 1
m = m * mult

# And that looks exactly like our condition for loop termination (the square of
# the next rational number is still less than 2.)
assert 2 * m**2 > n**2
assert loop_will_terminate(n, m)


# Remark: you might do away with the while-loop altogether, and replace it with
# a closed form solution like Rudin does in Ex. 1.A. This simplifies matters
# quite a bit. q = (2p + 2) / (p + 2)

# However, in situations like these, it's not clear to me that one can always
# find a neat closed-form solution to a repeating process as defined above (and
# guarantee it's rational).

# So in the moment, it felt more natural to define a process which must produce
# a reasonable answer and then reason about whether that process terminates or
# not.
