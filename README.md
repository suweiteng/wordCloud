

用python进行文本分词并生成词云


## 安装

* `pip3 install jieba`
* `pip3 install wordcloud`


# 运行
* 运行demo.py,会生成相应的的词云图，和“doc/词频统计.txt”  
* `python3 demo.py`



## 说明


* 新增词语请写入字典，如不想分割的人名。字典：userdict/userdict.txt

* 默认无意义词库，如'着'等。可自行添加不想纳入统计的词语，：userdict/stopword.txt


