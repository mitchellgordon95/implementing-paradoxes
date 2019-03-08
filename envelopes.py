import random

prefers_left = 0
# prefers_right is TRIALS - prefers_left
# left_then_switch is the same as prefers right
# right_then_switch is the same as prefers left
doesnt_care = 0
# doesnt_care_then_switch is TRIALS - doesnt_care

TRIALS = 1000000
for _ in range(TRIALS):
    x = random.randint(1, 100)
    y = 2 * x
    choices = [x,y]
    random.shuffle(choices)
    if choices[0] > choices[1]:
        prefers_left += 1
    if random.choice(choices) == max(choices):
        doesnt_care += 1

print('Prefers Left (aka Right then Switch): {}'.format(float(prefers_left) / TRIALS))
print('Prefers Right (aka Left then Switch): {}'.format(float(TRIALS - prefers_left) / TRIALS))
print('Doesn\'t Care: {}'.format(float(doesnt_care) / TRIALS))
print('Doesn\'t Care Then Switch: {}'.format(float(TRIALS - doesnt_care) / TRIALS))
