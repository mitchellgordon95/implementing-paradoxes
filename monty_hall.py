import numpy as np

# car is 0, goat is 1 and 2
trials = 10000000
correct = 0
for i in range(trials):
    choice = np.random.randint(3)
    # If we get it right first time
    if choice == 0:
        pass # Then we switch and don't get the car
    else:
        correct += 1 # Otherwise we switch and get the car

print(correct / trials * 100)
