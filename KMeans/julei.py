import numpy as np

class KMeans:
    def __init__(self,data,num_k):
        self.data = data
        self.num_k = num_k
    # 训练，max_iterations为最大迭代次数
    def train(self,max_iterations):
        # 1.随机选择K个中心点
        centroids = KMeans.centroids_init(self.data,self.num_k)
        # 2.开始训练
        num_examples = self.data.shape[0]
        closest_centroids_ids = np.empty((num_examples,1))
        for _ in range(max_iterations):
            # 3.得到当前每个样本点到中心点的距离，找到最近的
            closest_centroids_ids = KMeans.centroids_find_closest(self.data,centroids)
            # 4.进行中心点位置更新
            centroids = KMeans.centroids_compute(self.data,closest_centroids_ids,self.num_k)
        return centroids,closest_centroids_ids

    # 获取质心点
    @staticmethod
    def centroids_init(data,num_k):
        # data.shape[0]表示行数
        num_examples = data.shape[0]
        # 返回一个数组（随机数数组）
        random_ids = np.random.permutation(num_examples)
        centroids = data[random_ids[:num_k],:]
        return centroids

    @staticmethod
    def centroids_find_closest(data,centroids):
        num_examples = data.shape[0]
        num_centroids = centroids.shape[0]
        # np.zeros((n,m))返回一个数组n*m
        closest_centroids_ids = np.zeros((num_examples,1))
        # 样本点
        for example_index in range(num_examples):
            distance = np.zeros((num_centroids,1)) # 用于保存每个样本点到各个簇的距离
            # 簇的个数
            for centroids_index in range(num_centroids):
                distance_diff = data[example_index,:] - centroids[centroids_index,:]
                # 欧式距离（x1,y1）,(x2,y2)，distance = (x2 - x1)^2+(y2 - y2)^2
                distance[centroids_index] = np.sum(distance_diff**2)
            # 将样本归属于对应簇
            closest_centroids_ids[example_index]=np.argmin(distance)

        return closest_centroids_ids

    @staticmethod
    def centroids_compute(data,closest_centroids_ids,num_clustres):
        num_features = data.shape[1]
        centroids = np.zeros((num_clustres,num_features))
        for centroids_id in range(num_clustres):
            closest_ids = closest_centroids_ids == centroids_id
            centroids[centroids_id] = np.mean(data[closest_ids.flatten(),:],axis = 0)
        return centroids