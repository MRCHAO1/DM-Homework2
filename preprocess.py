import matplotlib.pyplot as plt

# 读取文本文件
data_list = []
with open('dataCV.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            if line.split(',')[0] == 'V':
                _, data, _ = line.split(',')
                data_list.append(int(data))

# 统计频率最高的元素
frequencies = {}
for data in data_list:
    frequencies[data] = frequencies.get(data, 0) + 1

most_common = max(frequencies, key=frequencies.get)
print("频率最高的元素:", most_common)

# 统计数据大小的频率分布
data_freq = []
for data in range(min(data_list), max(data_list) + 1):
    data_freq.append(frequencies.get(data, 0))

# 绘制数据大小分布的折线图
plt.plot(range(min(data_list), max(data_list) + 1), data_freq)
plt.xlabel('Data')
plt.ylabel('Times')
plt.title('Range')
plt.grid(False)
plt.show()
