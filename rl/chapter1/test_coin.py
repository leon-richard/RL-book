from collections import Counter
import unittest

# from abc import ABC, abstractmethod
from dataclasses import dataclass
import random
import statistics
# from typing import Generic, TypeVar, Sequence
from typing import Callable

from rl.distribution import Distribution

# from rl.distribution import (Bernoulli, Categorical, Choose, Constant,
#                              Gaussian, SampledDistribution, Uniform)

@dataclass(frozen=True)
class Coin(Distribution[str]):
    def sample(self):
        return "heads" if random.random() < 0.5 else "tails"
    
    def expectation(
        self,
        f: Callable[[str], float]
    ) -> float:
        return statistics.mean(f(self.sample()) for _ in range(1000))

def payoff(x: str) -> float:
    return 1.0 if x == 'heads' else 0.0

class TestDistribution(unittest.TestCase):
    def setUp(self):
        self.coin = Coin()

    def test_expectation(self):
        expected_coin = self.coin.expectation(payoff)
        print(f'expected_coin = {expected_coin}')
        self.assertTrue(0 <= expected_coin <= 1.0)

        expected_coin = self.coin.expectation(lambda coin: 1.0 if coin == "heads" else 0.0)
        print(f'expected_coin = {expected_coin}')
        self.assertTrue(0 <= expected_coin <= 1.0)


    def test_sample_n(self):
        samples = self.coin.sample_n(10)
        # print(f'samples = {samples}')
        self.assertEqual(len(samples), 10)
        self.assertTrue(all(s in ("heads" "tails") for s in samples))