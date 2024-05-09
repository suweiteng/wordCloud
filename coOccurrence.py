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
    top_words = word_counts.most_common(50)  # 示例中使用所有词，实际应设定如most_common(50)

    # 创建单词到索引的映射，仅包含高频词汇
    word_to_index = {word: idx for idx, (word, _) in enumerate(top_words)}

    # print((word_to_index))
  
    # 过滤words，只保留出现在top_words中的词
    filtered_words = [word for word in words if word in word_to_index]
    print((filtered_words))
    # 构建并显示共现矩阵
    cooccurrence_matrix = build_cooccurrence_matrix(filtered_words, word_to_index)

    plt.figure(figsize=(10, 8))
    plt.rcParams['font.sans-serif']=['Hiragino Sans GB'] # 修改字体
    plt.rcParams['axes.unicode_minus'] = False # 正常显示负号 
    sns.heatmap(cooccurrence_matrix, annot=True, fmt='g', cmap='coolwarm', xticklabels=[word for word, _ in top_words], yticklabels=[word for word, _ in top_words])
    plt.title('Words Co-occurrence Matrix')
    plt.xlabel('Words')
    plt.ylabel('Words')
    plt.show()

# 构建共现矩阵
def build_cooccurrence_matrix(filtered_words, word_to_index):
    cooccur_matrix = defaultdict(lambda: defaultdict(int))
    
    # 确保只处理存在于高频词汇列表中的词语，并避免重复计数
    for i in range(len(filtered_words) - 1):
        word1 = filtered_words[i]
        word2 = filtered_words[i + 1]
        if word1 in word_to_index and word2 in word_to_index:
            cooccur_matrix[word_to_index[word1]][word_to_index[word2]] += 1

    vocab_size = len(word_to_index)
    matrix = np.zeros((vocab_size, vocab_size), dtype=int)
    for i, row in enumerate(cooccur_matrix.values()):
        for j, count in row.items():
            matrix[i, j] = count
            
    return matrix





# 