from probability import Die, Coin, expected_value, Gaussian
from dataclasses import replace
from statistics import mean
import time

die_1 = Die(6)
die_2 = Die(8)

print(die_1)

print(die_1 == die_2)

die_3 = replace(die_2, sides=3)

print(die_2)
print(die_3)

foo = Die('Foo')
# x = foo.sample()

coin = Coin()
print(list(coin.sample() for _ in range(10)))

die_x = Die(8.8)
# print(expected_value(die_x, 1000))
# print(type(die_x.sample()))

samples = die_1.sample_n(100)
print(samples)
print(mean(samples))

gaussian = Gaussian(0.0, 1.0)
print(gaussian.sample())
gaussian_samples = gaussian.sample_n(10)
print(gaussian_samples)

start_time = time.time()

[gaussian.sample() for _ in range(1000000)]

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码执行时间: {elapsed_time:.2f} 秒")

start_time = time.time()

gaussian.sample_n(1000000)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码执行时间: {elapsed_time:.2f} 秒")

beta = 'β'
print(beta)

