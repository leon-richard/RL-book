from rl.distribution import Categorical, Constant
from rl.markov_process import FiniteMarkovProcess, NonTerminal
import numpy as np
import itertools

tran_map = {"Rain": Categorical({"Rain": 0.3, "Nice": 0.7}),
    "Snow": Categorical({"Rain": 0.4, "Snow": 0.6}),
    "Nice": Categorical({"Rain": 0.2, "Snow": 0.3, "Cloudy": 0.55})  # 增加一个Cloudy的terminal状态
}

print(tran_map)

finiteMarProc = FiniteMarkovProcess(transition_map=tran_map)
print(finiteMarProc)

traces_gen = finiteMarProc.traces(start_state_distribution=Constant(NonTerminal("Nice")))  # 从固定的NonTerminal 状体开始，用Constant分布

num_traces = 10
# num_steps = 60

# 生成 num_traces 条随机过程，每个过程都直到 Terminal 状态才结束。（如果tran_map中没有Terminal状态，则只有使用num_steps的方式来截断iterator的数据生成）
traces = [
    [s.state for s in proc] for proc in itertools.islice(traces_gen, num_traces)
]

# print(traces)

for tra in traces:
    print(len(tra))
    print(tra)