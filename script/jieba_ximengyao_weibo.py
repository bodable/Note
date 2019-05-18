# -*- coding: UTF-8 -*-
import jieba.analyse

path = 'ximengyao.txt'
file_in = open(path, 'r')
content = file_in.read()

try:
    # jieba.analyse.set_stop_words('你的停用词表路径')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        #权重是小数，为了凑整，乘了一万
        print(v + '\t' + str(int(n * 10000)))

finally:
    file_in.close()
