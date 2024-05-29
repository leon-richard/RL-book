from typing import Generic, TypeVar
from abc import ABC
from dataclasses import dataclass

T = TypeVar('T')
S = TypeVar('S')

@dataclass #(frozen=True)
class Container(Generic[T, S]):
    key: T
    value: S
    def get_value(self) -> S:
        return self.value
    def get_key(self) -> T:
        return self.key

# 使用泛型类
int_container = Container(42, 'myValue') 
str_container = Container[str, int]("hello", 55)

print(int_container.get_value())  # 输出: 42
print(str_container.get_value())  # 输出: hello

str_container.value = 33
print(str_container.get_value())  # 输出: 42