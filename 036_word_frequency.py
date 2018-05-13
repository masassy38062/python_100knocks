#36. 単語の出現頻度
#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

#-*-coding:utf-8-*-

import codecs
import ast
import collections
import operator

if __name__ == "__main__":

    with codecs.open('neko.txt.mecab.analyze','r','utf-8') as f:
        temp_lines = f.readlines()

    temp_list = []
    temp_dict = {}
    for temp_line in temp_lines:
        temp_dict = ast.literal_eval(temp_line)
        temp_word = temp_dict['surface']
        temp_list.append(temp_word)

    count_dict = collections.Counter(map(str,temp_list))

    for value,count in sorted(count_dict.items(),key=operator.itemgetter(1),reverse=True):
        print(count,value)

