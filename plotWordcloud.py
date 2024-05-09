# coding:utf-8

from os import path
from PIL import Image
from wordcloud import WordCloud
import numpy as np

stopwords_path = 'userdict/stopword.txt'
def generate_wordcloud(text):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    # print(text)
    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask1.jpg")))
    font_path=path.join(d,"font//msyh.ttf")
    wc = WordCloud(
        background_color="white",# 设置背景颜色  "silver"
        color_func=lambda *args, **kwargs: "black" , # 设置字体颜色 
        stopwords=stopwords_path, # 设置停用词 无法为空，因此再设置一次停用词
            max_words=100, # 词云显示的最大词数  
            collocations=False, #可防止出现重复
            # width=600,  # 宽度
            # height=400,   # 高度
            max_font_size=150, #最大字的最大字体大小
            min_font_size=10, #最小字体大小
           mask=alice_mask,# 设置背景图片       
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
           prefer_horizontal=1.01, # 文字横向和竖向之比，当大于1时文字全部横着。默认为0.9
        )
    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "Images//alice.png"))






# 