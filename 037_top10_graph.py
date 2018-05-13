#37. 頻度上位10語
#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

# -*-coding:utf-8-*-

import codecs
import ast
import collections
import operator
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

if __name__ == "__main__":

    with codecs.open('neko.txt.mecab.analyze', 'r', 'utf-8') as f:
        temp_lines = f.readlines()

    temp_list = []
    temp_dict = {}
    for temp_line in temp_lines:
        temp_dict = ast.literal_eval(temp_line)
        temp_word = temp_dict['surface']
        temp_list.append(temp_word)

#リストを要素ごとにカウントした値を辞書型へ入れ込む
    count_dict = collections.Counter(map(str, temp_list))

    i = 0
    size = 10
    graph_y_list = []
    graph_x_list = []
    for value, count in sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True):
        if(i < size):
            graph_y_list.append(count)
            graph_x_list.append(value)
            i += 1

#日本語の設定
    fp = FontProperties(fname=r'/Library/fonts/ipag.ttf', size=11)
#グラフのパラメータ
    plt.title("37.top10", fontproperties=fp)
    plt.xlabel('出現頻度が多い10単語', fontproperties=fp)
    plt.ylabel('出現頻度数', fontproperties=fp)

#X軸
    x = np.arange(len(graph_x_list))
    plt.xticks(x,graph_x_list,fontproperties=fp)
#Y軸
    y = np.array(graph_y_list)

#matplotlib.pyplot.bar(x=left_list, y=height_list)
    plt.bar(x,y)

#グラフの表示
    plt.show()


