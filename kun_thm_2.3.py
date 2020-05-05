import matplotlib.pyplot as plt

def polynomial(*coeffs):
    def poly(x):
        # return sum([coeff * x**i for i in enumerate(coeffs)])
        total = 0
        for i, coeff in enumerate(coeffs):
            total += coeff * x**i
        return total
    return poly


p_1 = polynomial(1, 1, 1)

plt.plot(range(-10, 10), [p_1(x) for x in range(-10,10)])
plt.show()
