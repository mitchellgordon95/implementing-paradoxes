from math import exp
def softmax(X):
    exponents = [exp(x) for x in X]
    summation = sum(exponents)
    return [x / summation for x in exponents]

# Conjecture: softmax is invariant under addition of a constant
# softmax(x) = softmax(x + c)
print softmax([1, 2])
print softmax([101, 102])
print softmax([.1, 1.1])
print softmax([-1, 0])
print
print softmax([1, 3])
print softmax([101, 103])
print
print softmax([1, 2, 3])
print softmax([101, 102, 103])
print 
# In other words, the only thing that matters to softmax is the difference
# between the values, not the values themselves.

# Note also that the derivative of softmax can be expressed in terms of softmax.
# See https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/

# d/dxi softmax(X)[j] = softmax(X)[i] * softmax(X)[j]

# If softmax is invariant under addition, then its derivative is also invariant under addition.

# So for high values of X, the derivatives should be the same as for low values of X with the same absolute differences.

# However, if your X values are around 100, then a difference of 1 seems small. My guess is that in the paper,
# the high values of X were accompanied by a high variance. So, they'd have something like 100 vs. 107, which maxes out softmax
# and results in no gradient.
print "It only takes an difference of 7 to basically max out softmax, no matter the scale of the inputs"
print softmax([100, 107])
print softmax([0, 7])
