from rl.distribution import (Constant, FiniteDistribution, Bernoulli, Range, Choose, Categorical)
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

die = Categorical({1: 1/6, 2: 1/6, 3: 1/6, 4: 1/12, 5: 1/12, 6: 2/6})
print(die.sample())
print(die.sample_n(30))
print(die.probability(1))
print(die.probability(2))
print(die.probability(9))
print(die.table())
print(die.expectation(lambda X: X))

die_samples = die.sample_n(100000)
samples_distribution = Counter(die_samples)
print(samples_distribution)

# 创建一个图形对象
# plt.figure(figsize=(10, 6))
bins = 6
plt.hist(die_samples, bins=bins, edgecolor='black', density=True)
plt.ylim(0.0, 1.0)

# 添加标题和标签
plt.title('Histogram of Samples')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('die.png')