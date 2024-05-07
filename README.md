

用python进行文本分词并生成词云，支持txt和docx格式文件。

## 安装

* `pip3 install jieba`
* `pip3 install wordcloud`
* `pip3 install python-docx`


# 运行
* 请将文本放入doc文件夹。运行demo.py,会生成相应的的词云图，和“doc/词频统计.txt”。默认读取demo.txt 如有运行时命令有附加参数d，则读取demo.docx。  

* txt文件命令： `python3 demo.py` 
* docx文件命令： `python3 demo.py d`


## 说明

* 如部分人名等词语被误拆分，可以将其写入词典。路径：userdict/userdict.txt

* 部分字词属于统计上意义较小的词库，如'着' '的' 等。本仓库已内置了一些字词。如仍有不想纳入统计的词语，可自行添加。路径：userdict/stopword.txt

* 

![image](https://raw.githubusercontent.com/suweiteng/wordCloud/master/Images/alice.png)  
