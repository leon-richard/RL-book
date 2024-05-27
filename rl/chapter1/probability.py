from abc import ABC, abstractmethod
from dataclasses import dataclass
import random
import statistics
from typing import Generic, TypeVar, Sequence


A = TypeVar("A")


class Distribution(ABC, Generic[A]):
    @abstractmethod
    def sample(self) -> A:
        pass

    def sample_n(self, n: int) -> Sequence[A]:
        return [self.sample() for _ in range(n)]


class OldDie(Distribution):
    def __init__(self, sides):
        self.sides = sides

    def __repr__(self):
        return f"Die(sides={self.sides})"

    def __eq__(self, other):
        if isinstance(other, Die):
            return self.sides == other.sides

        return False

    def sample(self) -> int:
        return random.randint(1, self.sides)


six_sided = OldDie(6)


def roll_dice():
    return six_sided.sample() + six_sided.sample()


@dataclass(frozen=True)
class Coin(Distribution[str]):
    def sample(self):
        return "heads" if random.random() < 0.5 else "tails"


@dataclass(frozen=True)
class Die(Distribution[int]):
    sides: int

    def sample(self):
        return random.randint(1, self.sides)


def expected_value(d: Distribution[float], n: int) -> float:
    return statistics.mean(d.sample() for _ in range(n))

import numpy as np
@dataclass
class Gaussian(Distribution[float]):
    μ: float
    σ: float
    def sample(self) -> float:
        return np.random.normal(loc=self.μ, scale=self.σ)
    def sample_n(self, n: int) -> Sequence[float]:
        return list(np.random.normal(loc=self.μ, scale=self.σ, size=n))


expected_value(Die(6), 100)

