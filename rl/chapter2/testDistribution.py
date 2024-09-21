from rl.distribution import (Constant, FiniteDistribution, Bernoulli, Range, Choose, Categorical)

constantDistribution = Constant(3.14)

print(constantDistribution)
print(constantDistribution.sample())
print(constantDistribution.sample_n(10))
print(constantDistribution.probability(3.14))
print(constantDistribution.table())
print(constantDistribution.expectation(lambda X: X))

bernoulli = Bernoulli(0.7)
print(bernoulli)
print(bernoulli.sample())
print(bernoulli.sample_n(10))
print(bernoulli.probability(True))
print(bernoulli.probability(False))
print(bernoulli.table())
print(bernoulli.expectation(lambda X: 1.0 if X == True else 0.0))

range = Range(0, 5)
print(range)
print(range.sample())
print(range.sample_n(20))
print(range.probability(0))
print(range.probability(1))
print(range.probability(9))
print(range.table())
print(range.expectation(lambda X: X))

choose = Choose((1, 2, 3, 1, 1))
print(choose)
print(choose.sample())
print(choose.sample_n(30))
print(choose.probability(1))
print(choose.probability(2))
print(choose.probability(9))
print(choose.table())
print(choose.expectation(lambda X: X))

categorical = Categorical({1: 0.3, 2: 0.5, 3: 0.2})
print(categorical.sample())
print(categorical.sample_n(30))
print(categorical.probability(1))
print(categorical.probability(2))
print(categorical.probability(9))
print(categorical.table())
print(categorical.expectation(lambda X: 2*X))