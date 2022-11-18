import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from julei import KMeans
#data = pd.read_csv("iris.csv")
data = pd.read_excel("julei20221116.xlsx")
iris_types = ["setosa","virginica","versicolor"]
#x_axis = "Sepal.Width"
#y_axis = "Petal.Length"
x_axis = "语音次数"
y_axis = "短信数"


"""
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
for iris_type in iris_types:
    plt.scatter(data[x_axis][data["Species"]==iris_type],data[y_axis][data["Species"]==iris_type],label = iris_type)
plt.title("label known")
plt.legend()

plt.subplot(1,2,2)
plt.scatter(data[x_axis][:],data[y_axis][:])
plt.title("label unknown")
plt.show()
"""
num_examples = data.shape[0]
# reshape就是变成一个我们指定的数组reshape(num_examples,2)-》num_examples*2
x_train = data[[x_axis,y_axis]].values.reshape(num_examples,2)

# 指定好训练用的参数
# 设置三个簇
num_clustres = 3
# 设置迭代数
max_iteritions = 50

k_means = KMeans(x_train,num_clustres)
centroids,closest_centroids_ids = k_means.train(max_iteritions)

plt.figure(figsize=(12,5))
# plt.subplot(1,2,1)
# for iris_type in iris_types:
#     plt.scatter(data[x_axis][data["Species"]==iris_type],data[y_axis][data["Species"]==iris_type],label = iris_type)
# plt.title("label know")
# plt.legend()
plt.subplot(1,1,1)
for centroid_id,centroid in enumerate(centroids):
    # 拿索引
    current_examples_index = (closest_centroids_ids == centroid_id).flatten()
    plt.scatter(data[x_axis][current_examples_index], data[y_axis][current_examples_index], label=centroid_id)

for centroid_id,centroid in enumerate(centroids):
    plt.scatter(centroid[0],centroid[1],c="black",marker="x")
plt.legend()
plt.title("label kmeans")
plt.show()