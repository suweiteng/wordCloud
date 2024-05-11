# coding:utf-8


from collections import defaultdict, Counter
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

stopwords_path = 'userdict/stopword.txt'
def generate_pic(text):

       
    # 初始化矩阵
    words = text.split()
    # 统计词频并选择全部词，实际应用中应根据需要筛选高频词汇
    word_counts = Counter(words)
    top_words = word_counts.most_common(31)  # 选取最高频的前N个词语。

    # 创建单词到索引的映射，仅包含高频词汇，
    word_to_index = {word: idx for idx, (word, _) in enumerate(top_words)} # word_to_index用于矩阵坐标轴 
    word_to_index_new =  {value: key for key, value in word_to_index.items()}
    # print((word_to_index))
    # 构建并显示共现矩阵
    cooccurrence_matrix = build_cooccurrence_matrix(words, word_to_index)
  
    #生成共现矩阵热力图
    generate_cooccurrence_matrix(cooccurrence_matrix,top_words);

    #生成共现矩阵关系图
    generate_cooccurrence_network(cooccurrence_matrix,1,word_to_index_new);
    

# 构建共现矩阵
def build_cooccurrence_matrix(filtered_words, word_to_index):
    
    cooccur_matrix = np.zeros((len(word_to_index), len(word_to_index)), dtype=int)
    
    for i in range(len(filtered_words) - 1):
        word1 = filtered_words[i]
        word2 = filtered_words[i + 1]
        if word1 in word_to_index and word2 in word_to_index:
            index1, index2 = word_to_index[word1], word_to_index[word2]
            cooccur_matrix[index1][index2] += 1
            cooccur_matrix[index2][index1] += 1  # 确保矩阵对称性

    # 将对角线元素设为0
    np.fill_diagonal(cooccur_matrix, 0)

    return cooccur_matrix


# 生成共现矩阵热力图
def generate_cooccurrence_matrix(cooccurrence_matrix, top_words):
    plt.figure(figsize=(10, 8))
    plt.rcParams['font.sans-serif']=['Hiragino Sans GB'] # 修改字体
    plt.rcParams['axes.unicode_minus'] = False # 正常显示负号 
    sns.heatmap(cooccurrence_matrix, annot=True, fmt='g', cmap='coolwarm', xticklabels=[word for word, _ in top_words], yticklabels=[word for word, _ in top_words])
    plt.title('共现矩阵热力图')
    plt.xlabel(' ')
    plt.ylabel(' ')
    # 使用savefig方法保存图片
    print("共现矩阵热力图:images/my_figure.png")
    plt.savefig('images/my_figure.png')
    #plt.show()

# 生成共现矩阵关系图
def generate_cooccurrence_network(cooccurrence_matrix, min_threshold,word_to_index):
    # 过滤掉共现次数低于阈值的边
    G = nx.from_numpy_array(cooccurrence_matrix)
    G.remove_edges_from([(u, v) for u, v, d in G.edges(data=True) if d['weight'] < min_threshold])
    # 定义函数来获取节点的标签（词汇）
    def get_node_label(node_id):
        return word_to_index.get(node_id, str(node_id))  # 如果找不到对应的词汇，返回节点ID作为备选

    # 为每个节点生成标签
    labels = {node: get_node_label(node) for node in G.nodes()}
    # 生成网络图布局
    pos = nx.spring_layout(G, seed=42)

    # 绘制共现矩阵关系图
    plt.figure(figsize=(12, 8))
    plt.title('共现矩阵关系图')
    plt.rcParams['font.sans-serif']=['Hiragino Sans GB'] # 修改字体
    plt.rcParams['axes.unicode_minus'] = False # 正常显示负号 
    nx.draw_networkx_nodes(G, pos, node_size=500, alpha=0.8)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos,labels=labels, font_size=10, font_family='Hiragino Sans GB')
    
    # 显示图中的权重（可选）
    # = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight_labels)
    
    print("共现矩阵关系图:images/diagram.png")
    plt.savefig('images/diagram.png')
    plt.axis('off')  # 关闭坐标轴
    #plt.show()
