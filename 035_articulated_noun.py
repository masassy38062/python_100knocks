#35. 名詞の連接
#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

#-*-coding:utf-8-*-

import codecs
import ast

if __name__ == "__main__":
    with codecs.open('neko.txt.mecab.analyze','r','utf-8') as f:
        temp_lines = f.readlines()

    temp_dict={}
    temp_word = ''
    temp_list = []
    articulated_noun_list = []
    flag=0

    for temp_line in temp_lines:
        temp_dict = ast.literal_eval(temp_line)
        if(temp_dict['pos']=='名詞' and flag ==0):
            temp_word = temp_dict['surface']
            flag = 1
            continue

        elif(temp_dict['pos']=='名詞' and flag >= 1):
            temp_word += temp_dict['surface']
            flag += 1
            continue

        elif(temp_dict['pos']!='名詞' and flag >= 2):
            temp_list.append(temp_word)
            temp_word = ''
            flag = 0
            continue

        else:
            temp_word=''
            flag =0
            continue

    articulated_noun_list = set(temp_list)

    for temp in articulated_noun_list:
        print(temp)
