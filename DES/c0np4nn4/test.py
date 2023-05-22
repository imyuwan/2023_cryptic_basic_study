from IP import *

# IP Test
init_state = list(range(1, 65))
state_1 = initial_permutation(init_state)
state_2 = inverse_permutation(state_1)
assert(init_state == state_2)

