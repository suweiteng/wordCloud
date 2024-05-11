# coding:utf-8


from collections import defaultdict, Counter
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


stopwords_path = 'userdict/stopword.txt'
def generate_wordcloud(text):

       
    # 初始化矩阵
    words = text.split()
    # 统计词频并选择全部词，实际应用中应根据需要筛选高频词汇
    word_counts = Counter(words)
    top_words = word_counts.most_common(31)  # 选取最高频的前N个词语。

    # 创建单词到索引的映射，仅包含高频词汇，
    word_to_index = {word: idx for idx, (word, _) in enumerate(top_words)} # word_to_index用于矩阵坐标轴 
    # print((word_to_index))

    # print(("------------"))
    # print((words))

    # 构建并显示共现矩阵
    cooccurrence_matrix = build_cooccurrence_matrix(words, word_to_index)

    plt.figure(figsize=(10, 8))
    plt.rcParams['font.sans-serif']=['Hiragino Sans GB'] # 修改字体
    plt.rcParams['axes.unicode_minus'] = False # 正常显示负号 
    sns.heatmap(cooccurrence_matrix, annot=True, fmt='g', cmap='coolwarm', xticklabels=[word for word, _ in top_words], yticklabels=[word for word, _ in top_words])
    plt.title('Words Co-occurrence Matrix')
    plt.xlabel('Words')
    plt.ylabel('Words')
    # 使用savefig方法保存图片
    plt.savefig('images/my_figure.png')
    #plt.show()

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
            
    return cooccur_matrix





# 