from abc import ABC, abstractmethod
from typing import (Generic, TypeVar)
from dataclasses import dataclass

S = TypeVar('S')

class State(ABC, Generic[S]):
    state: S

# @dataclass(frozen=True)
class Terminal(State, Generic[S]):
    state1: S
    def __init__(self, argue1: S, argue2: S) -> None:
        super().__init__()
        self.state = argue1
        self.state1 = argue2

terminal = Terminal(123, 'soiewj')
print(terminal)
print(terminal.state)