import pandas as pd
import scipy.stats as ss

df = pd.read_csv("./data/HR.csv")
print("--------平均----------")
print(df.mean())
print(df["satisfaction_level"].mean()) # 求平均数
print("--------中位----------")
print(df.median()) # 中位数
print("--------4分----------")
print(df.quantile(q=0.25)) # 四分位数
print("--------众数----------")
print(df.mode()) # 众数
print("--------标准----------")
print(df.std()) # 标准差
print("--------方差----------")
print(df.var()) # 方差
print("--------偏态----------")
print(df.skew()) # 偏态系数
print(df["satisfaction_level"].skew())# -0.47643761717258093 说明平均值偏小，负偏
print("--------峰态----------")
print(df["satisfaction_level"].kurt())# 正态分布为0，说明这个相对还是比较平缓的


print("------------------------------------------------------------")
print(ss.norm.stats(moments="mvsk")) # m:均值，v:方差，s偏态系数，k:峰态系数 # 正态分布
print(ss.norm.pdf(0.0)) # x为0输出纵坐标
print(ss.norm.ppf(0.9)) # 从负无穷到某个点概率为0.9输出点1.2815515655446004
print(ss.norm.cdf(2)) # 从-∞到2概率为多少0.9772498680518208
print("------------------------------------------------------------")
df.sample(n=10) # 抽样抽10个
