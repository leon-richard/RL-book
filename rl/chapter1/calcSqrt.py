from typing import Iterator
import itertools

def sqrt(a: float) -> float:
    x = a / 2 # initial guess
    x_n = a
    while abs(x_n - x) > 0.001:
        x = x_n
        x_n = (x + (a / x)) / 2
    return x_n

print(sqrt(3))
print(sqrt(100))

# for x in [3, 2, 1]: print(x)
# for x in {3, 2, 1}: print(x)
# for x in range(3): print(x)

def sqrt_iterator(a: float) -> Iterator[float]:
    x = a / 2 # initial guess
    while True:
        x = (x + (a / x)) / 2
        yield x

x_old = 0
for x in sqrt_iterator(300):
    print(x)
    if abs(x - x_old) < 0.00001:
        break
    x_old = x

iterations = list(itertools.islice(sqrt_iterator(30000), 10))
print(iterations)

def converge(values: Iterator[float], threshold: float) -> Iterator[float]:
    for a, b in itertools.pairwise(values):
        yield a
        if abs(a - b) < threshold:
            break

results = converge(sqrt_iterator(30000), 0.001)
capped_results = list(itertools.islice(results, 3))
print(capped_results)

results = itertools.islice(sqrt_iterator(30000), 100)
capped_results = list(converge(results, 0.001))
print(capped_results)