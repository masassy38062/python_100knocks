#34. 「AのB」
#2つの名詞が「の」で連結されている名詞句を抽出せよ．
#-*-coding:utf-8-*-

import codecs
import ast

if __name__ == "__main__":

    with codecs.open('neko.txt.mecab.analyze','r','utf-8') as f:
        temp_lines = f.readlines()

    flag = 0
    temp_list = []
    for temp_line in temp_lines:
        temp_dict = ast.literal_eval(temp_line)
        if (temp_dict['pos'] == '名詞' and flag == 0):
            temp_word = temp_dict['surface']
            flag = 1
            continue

        elif(temp_dict['surface']=='の' and temp_dict['pos']=='助詞' and flag == 1):
            temp_word += temp_dict['surface']
            flag = 2
            continue

        elif(temp_dict['pos']=='名詞' and flag == 2):
            temp_word += temp_dict['surface']
            temp_list.append(temp_word)
            temp_word = ''
            flag = 0
            continue

        else:
            temp_word=''
            flag =0
            continue

    no_noun_list = set(temp_list)


    for temp in no_noun_list:
        print(temp)





