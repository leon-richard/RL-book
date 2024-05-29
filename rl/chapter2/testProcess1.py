from stock_price_simulations import simulation, Process1, process1_price_traces

process = Process1(10, alpha1=0.2)

sim = simulation(process, Process1.State(price=3))

traces = process1_price_traces(3, 10, 0.2, 100, 30)

print(traces.shape)

import matplotlib.pyplot as plt

# 创建一个图形对象
plt.figure(figsize=(10, 6))

# 遍历每一行数据并绘制曲线
data = traces
for i in range(data.shape[0]):
    plt.plot(data[i], label=f'Curve {i+1}')

# 添加图例（可选）
# plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# 添加标题和标签
plt.title('30 Curves with 100 Points Each')
plt.xlabel('Point Index')
plt.ylabel('Value')

# 显示图形
# plt.show()
plt.savefig('plot.png')  # 保存图形为文件

y = 0.7
x: int = round(y)
print(x)