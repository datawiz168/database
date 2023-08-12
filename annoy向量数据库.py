from annoy import AnnoyIndex
import random

# 定义向量的维度
dimension = 40

# 创建Annoy索引
index = AnnoyIndex(dimension, 'angular')

# 添加1000个随机向量到索引
for i in range(1000):
    v = [random.gauss(0, 1) for _ in range(dimension)]
    index.add_item(i, v)

# 构建索引，10棵树
index.build(10)

# 保存索引到磁盘
index.save('test_index.ann')

# 加载索引
loaded_index = AnnoyIndex(dimension, 'angular')
loaded_index.load('test_index.ann')

# 查询最近的5个邻居
query_vector = [random.gauss(0, 1) for _ in range(dimension)]
nns = loaded_index.get_nns_by_vector(query_vector, 5)

print('最近的5个邻居:', nns)


'''
说明
    AnnoyIndex(dimension, 'angular')创建了一个Annoy索引，其中dimension是向量的维度，'angular'是距离度量（在这种情况下是角距离）。
    使用add_item方法将向量添加到索引中。
    使用build方法构建索引。
    可以使用save和load方法将索引保存到磁盘并从磁盘加载。
    get_nns_by_vector方法用于查询最近的邻居。

这个例子显示了Annoy的基本用法，包括创建索引、添加项、构建、保存/加载和查询。根据您的具体需求和数据集，您可能需要调整参数和设置。

'''



