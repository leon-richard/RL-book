from dataclasses import dataclass
from typing import Mapping, Dict
from rl.distribution import Categorical, FiniteDistribution
from rl.markov_process import FiniteMarkovProcess
from scipy.stats import poisson
import graphviz


@dataclass(frozen=True)
class InventoryState:
    on_hand: int
    on_order: int

    def inventory_position(self) -> int:
        return self.on_hand + self.on_order


class SimpleInventoryMPFinite(FiniteMarkovProcess[InventoryState]):

    def __init__(
        self,
        capacity: int,
        poisson_lambda: float
    ):
        self.capacity: int = capacity
        self.poisson_lambda: float = poisson_lambda

        self.poisson_distr = poisson(poisson_lambda)
        super().__init__(self.get_transition_map())

    def get_transition_map(self) -> \
            Mapping[InventoryState, FiniteDistribution[InventoryState]]:
        d: Dict[InventoryState, Categorical[InventoryState]] = {}
        for alpha in range(self.capacity + 1):
            for beta in range(self.capacity + 1 - alpha):
                state = InventoryState(alpha, beta)
                ip = state.inventory_position()
                beta1 = self.capacity - ip
                state_probs_map: Mapping[InventoryState, float] = {
                    InventoryState(ip - i, beta1):
                    (self.poisson_distr.pmf(i) if i < ip else
                     1 - self.poisson_distr.cdf(ip - 1))
                    for i in range(ip + 1)
                }
                d[InventoryState(alpha, beta)] = Categorical(state_probs_map)
        return d
    
    def presentAlphaBeta(self, s: InventoryState) -> str:
        return f'α={s.on_hand}, β={s.on_order}'
    
    def generate_image(self) -> graphviz.Digraph:
        d = graphviz.Digraph()

        for s in self.transition_map.keys():
            d.node(self.presentAlphaBeta(s.state))

        for s, v in self.transition_map.items():
            for s1, p in v:
                d.edge(self.presentAlphaBeta(s.state), self.presentAlphaBeta(s1.state), label=f"{p:.1%}")

        return d

import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    user_capacity = 2
    user_poisson_lambda = 1.0

    # 生成x轴的值
    x = np.arange(0, 10)

    # 计算每个x值的PMF
    pmf = poisson.pmf(x, user_poisson_lambda)

    # 画出PMF
    plt.bar(x, pmf)
    plt.xlabel('Number of events (k)')
    plt.ylabel('Probability')
    plt.title('Poisson PMF')
    plt.savefig('poisson.png')

    si_mp = SimpleInventoryMPFinite(
        capacity=user_capacity,
        poisson_lambda=user_poisson_lambda
    )

    print("Transition Map")
    print("--------------")
    print(si_mp)

    print("Stationary Distribution")
    print("-----------------------")
    si_mp.display_stationary_distribution()

    digraph = si_mp.generate_image()
    digraph.render('simpleInventoryMP', format='png', cleanup=True)
