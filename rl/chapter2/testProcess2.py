from stock_price_simulations import process2_price_traces

traces = process2_price_traces(start_price=100, alpha2=0.6, time_steps=200, num_traces=60)

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
plt.title(f'{data.shape[0]} Curves with {data.shape[1]} Points Each')
plt.xlabel('Point Index')
plt.ylabel('Value')

# 显示图形
# plt.show()
plt.savefig('plot.png')  # 保存图形为文件