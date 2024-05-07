

用python进行文本分词并生成词云，支持txt和docx格式文件。

## 安装

* `pip3 install jieba`
* `pip3 install wordcloud`
* `pip3 install python-docx`


# 运行
* 运行demo.py,会生成相应的的词云图，和“doc/词频统计.txt”  
* txt文件： `python3 demo.py` 
* docx文件： `python3 demo.py d`


## 说明


* 新增词语请写入字典，如不想分割的人名。路径：userdict/userdict.txt

* 默认无意义词库，如'着'等。可自行添加不想纳入统计的词语。路径：userdict/stopword.txt

* 默认读取demo.txt 如有附加参数d 则读取demo.docx

![image](https://raw.githubusercontent.com/suweiteng/wordCloud/master/Images/alice.png)  
