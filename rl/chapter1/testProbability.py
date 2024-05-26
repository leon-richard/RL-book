from probability import Die, Coin, expected_value
from dataclasses import replace

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