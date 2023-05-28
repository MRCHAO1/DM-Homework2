from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# 1代码首先将给定数据转换为适用于Apriori算法的格式。使用mlxtend库的TransactionEncoder将原始数据编码为二进制矩阵，
# 其中每个项被表示为布尔值。
# 2接下来，使用apriori函数应用Apriori算法来获取频繁项集。设置min_support参数为0.2，表示支持度阈值为0.2。
# 3然后，使用association_rules函数从频繁项集中获取关联规则。设置metric参数为"support"，表示使用支持度评估规则。
# 4对于导出的关联规则，代码计算支持度、置信度，并使用Lift和卡方进行评价。这些评价指标可以通过关联规则对象的属性进行访问，
# 如rules["support"]、rules["confidence"]、rules["lift"]和rules["chi_square"]。
# 5代码仅给出了一个简单的示例，实际数据和评价指标的选择需要根据具体情况进行调整。
# 此外，代码中使用的mlxtend库是一个常用的关联规则挖掘工具，可以根据实际需求选择其他工具或自行实现相关算法。

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from collections import Counter

def aprioriData(data, support, threshold):
    print('正在转换为适用于Apriori算法的格式……')
    # 转换为适用于Apriori算法的格式
    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    # print(df)
    print('正在使用Apriori算法获取频繁项集……')
    # 使用Apriori算法获取频繁项集
    frequent_itemsets = apriori(df, min_support=support, use_colnames=True)
    print('正在使用关联规则算法获取关联规则……')
    # 使用关联规则算法获取关联规则
    rules = association_rules(frequent_itemsets, metric="support", min_threshold=threshold)
    print('正在计算支持度和置信度……')
    # 计算支持度和置信度
    rules["support"] = rules["support"].round(2)
    rules["confidence"] = rules["confidence"].round(2)
    print('支持度：')
    print(rules["support"])
    print('置信度：')
    print(rules["confidence"])
    print('正在使用Lift评价关联规则……')
    # 使用Lift评价关联规则
    rules["lift"] = rules["lift"].round(2)
    print('正在计算卡方检验统计量并评价……')
    # 计算卡方检验统计量
    observed = rules["support"] * len(df)  # 观察到的频次
    expected = rules["antecedent support"] * rules["consequent support"] * len(df)  # 期望的频次
    chi_square = ((observed - expected) ** 2 / expected).sum()  # 卡方检验统计量
    # 使用卡方评价关联规则
    rules["chi_square"] = chi_square  # 添加卡方检验统计量到关联规则数据框
    # rules里面的各属性
    # antecedents: 关联规则的前项，即规则的左侧项集。
    # consequents: 关联规则的后项，即规则的右侧项集。
    # antecedent support: 前项的支持度，表示在数据集中出现前项的频率。
    # consequent support: 后项的支持度，表示在数据集中出现后项的频率。
    # support: 关联规则的支持度，表示在数据集中同时出现前项和后项的频率。
    # confidence: 关联规则的置信度，表示在前项出现的情况下，后项出现的概率。
    # lift: 关联规则的提升度，表示规则的信心相对于前项和后项独立出现的期望有多少增益。
    # leverage: 关联规则的杠杆度，表示规则的支持度减去前项和后项独立出现的期望。
    # conviction: 关联规则的确信度，表示规则的后项在前项出现的条件下相对于独立出现的期望有多大偏离。
    # zhangs_metric: 关联规则的 Zhang's Metric 值，表示规则的提升度和支持度之间的平衡度。
    # chi_square: 关联规则的卡方检验统计量，用于评估关联规则的质量。
    # 这些属性提供了关联规则的各种度量和评价指标，帮助我们了解规则的强度、相关性和质量。
    # 请注意，每个关联规则都有相应的前项、后项、支持度、置信度等属性值。您可以根据需求选择感兴趣的属性进行分析和解释。
    print("关联规则的lift：")
    print(rules["lift"])
    print("关联规则的chi_square：")
    print(rules["chi_square"])
    print("关联规则的antecedents: ")
    print(rules["antecedents"])
    print("关联规则的consequents: ")
    print(rules["consequents"])
    print("关联规则的antecedent support: ")
    print(rules["antecedent support"])
    print("关联规则的consequent support: ")
    print(rules["consequent support"])

def find_top_elements(lst, num):
    counter = Counter(lst)
    top_num = counter.most_common(num)
    return top_num

if __name__ == '__main__':
    dataA = []
    dataC = []
    dataV = []
    print('正在打开文件……')
    with open('./data.txt','r') as f:
        err = 0
        for line in f:
            category, id, title, url, caseID = '', '', '', '', ''
            line = line.strip('\n').split(',')
            if line[0] == 'A':
                if (len(line) < 5 or len(line) > 5):
                    err += 1
                else:
                    category = line[0]
                    id = line[1]
                    title = line[3]
                    url = line[4]
                    dataA.append([category, id, title, url])
            elif line[0] == 'C':
                if (len(line) < 3 or len(line) > 3):
                    err += 1
                else:
                    category = line[0]
                    caseID = line[2]
                    # dataC.append([category, caseID])
                    dataC.append(int(caseID))
            elif line[0] == 'V':
                if (len(line) < 3 or len(line) > 3):
                    err += 1
                else:
                    category = line[0]
                    id = line[1]
                    dataV.append([category, id])
        print('err: ' + str(err))
    print('Processing A……')
    aprioriData(dataA, 0.0001, 0.001)
    # print('Processing C……')
    # aprioriData(dataC, 0.00003, 0.00001)
    print('Processing V……')
    aprioriData(dataV, 0.001, 0.001)
    for element, count in find_top_elements(dataC, 10):
        print(f"元素 {element} 出现的频数为 {count}")

