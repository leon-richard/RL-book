from rl.distribution import Categorical
from typing import (Callable, Dict, Generic, Iterator, Iterable,
                    Mapping, Optional, Sequence, Tuple, TypeVar, List)
from collections import Counter
import matplotlib.pyplot as plt
# import numpy as np
from itertools import product
from collections import defaultdict

class Dice(Categorical):
    def __init__(self, distribution: Mapping[int, float] = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}):
        super().__init__(distribution)
    
    def __repr__(self) -> str:
        list_str = [f"{face}: {prob:.4f}" for face, prob in self]
        return ', '.join(list_str)

class N_Dies:
    list_dices: List[Dice]
    num_dices: int
    sum_dices: Dice

    def __init__(self, num_dices: int):
        self.list_dices = [Dice() for i in range(num_dices)]
        self.num_dices = len(self.list_dices)

        # dict_sum_dies = {}
        # for die in self.list_dies:

        self.sum_dices = Dice(self.calculate_probabilities())

    # 计算 n 个骰子的点数和及其概率
    def calculate_probabilities(self):
        # 用于存储点数和的概率
        sum_probabilities = defaultdict(float)

        # 使用 itertools.product 来生成每个骰子的所有可能结果的笛卡尔积
        possible_outcomes = product(*(dice.table().keys() for dice in self.list_dices))

        # 计算点数和及其概率
        for outcome in possible_outcomes:
            total_sum = sum(outcome)  # 计算点数和
            probability = 1
            for i, face in enumerate(outcome):
                probability *= self.list_dices[i].probability(face)  # 根据每个骰子的概率分布来计算概率
            # 将概率累加到相应的点数和
            sum_probabilities[total_sum] += probability

        return sum_probabilities
    
    def __repr__(self) -> str:
        list_str = [f'die_{i+1}:\n    {die}' for i, die in enumerate(self.list_dices)]
        return '\n'.join(list_str) + f'\nsum_dies:\n    {self.sum_dices}'
    
    def draw(self):
        # 创建一个图形对象
        # 提取骰子的面和对应的概率
        faces = list(self.sum_dices.table().keys())
        probabilities = list(self.sum_dices.table().values())

        # 画出概率分布的bar图
        plt.bar(faces, probabilities) #, color='blue')
        plt.xlabel('Sum of Dices')  # X轴标签
        plt.ylabel('Probability')  # Y轴标签
        plt.title(f'Probability Distribution of {self.num_dices} Dices')  # 标题
        plt.xticks(faces)  # X轴刻度
        plt.savefig('sum_dices.png')

n_dies = N_Dies(3)
print(n_dies)
n_dies.draw()
