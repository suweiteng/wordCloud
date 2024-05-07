# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_wordcloud(text):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask.png")))
    font_path=path.join(d,"font//msyh.ttf")
    wc = WordCloud(
        background_color="white",# 设置背景颜色  "silver"
        #color_func=lambda *args, **kwargs: "black" , # 设置字体颜色 
           max_words=300, # 词云显示的最大词数  
            width=1200,  # 宽度
            height=800,   # 高度
            max_font_size=150, #最大字的最大字体大小
            min_font_size=10, #最小字体大小
       #     mask=alice_mask,# 设置背景图片       
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )
    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "Images//alice.png"))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
#     plt.show()

