import random

prefers_left = 0
prefers_right = 0
# left_then_switch is the same as prefers right
# right_then_switch is the same as prefers left
doesnt_care = 0
doesnt_care_then_switch = 0

TRIALS = 1000000
for _ in range(TRIALS):
    choices = random.choice([[5, 10], [10, 20]])
    random.shuffle(choices)
    prefers_left += choices[0]
    prefers_right += choices[1]
    first_choice = random.randint(0, 1)
    doesnt_care += choices[first_choice]
    doesnt_care_then_switch += choices[0 if first_choice else 1]

print('Prefers Left (aka Right then Switch): {}'.format(float(prefers_left) / TRIALS))
print('Prefers Right (aka Left then Switch): {}'.format(float(prefers_right) / TRIALS))
print('Doesn\'t Care: {}'.format(float(doesnt_care) / TRIALS))
print('Doesn\'t Care Then Switch: {}'.format(float(doesnt_care_then_switch) / TRIALS))
