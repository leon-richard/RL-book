import numpy as np

samples = np.random.binomial(9, 0.1, 200000)

test_results = (samples == 0)

x = sum(test_results)/200000

print(f'x = {x}')

print(0.9**9)