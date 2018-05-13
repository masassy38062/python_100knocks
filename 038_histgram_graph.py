#39. ヒストグラム
#単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け
#-*-coding:utf-8-*-

import codecs
import ast
import collections
import operator
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

if __name__ == "__main__":
    with codecs.open('neko.txt.mecab.analyze','r','utf-8') as f:
        temp_lines = f.readlines()

    temp_list=[]
    temnp_dict={}
    temp_word = ''
    for temp_line in temp_lines:
        temp_dict = ast.literal_eval(temp_line)
        temp_word = temp_dict['surface']
        temp_list.append(temp_word)

    count_dict = {}
    count_dict = collections.Counter(map(str,temp_list))

    graph_x_list =[]
    graph_y_list =[]

    for key,value in sorted(count_dict.items(),key=operator.itemgetter(1),reverse=True):
        graph_x_list.append(key)
        graph_y_list.append(value)

# 日本語の設定
    fp = FontProperties(fname=r'/Library/fonts/ipag.ttf', size=11)
# グラフのパラメータ
    plt.title("38.ヒストグラム", fontproperties=fp)
    plt.xlabel('出現頻度', fontproperties=fp)
    plt.ylabel('単語の種類数', fontproperties=fp)

#matplotlib.pyplot.bar(y=data_list, bins=binの数, range=binの最小値と最大値,normed=y軸の値で正規化する)
    plt.hist(graph_y_list,bins=20,range=(1,20),normed=True)

#グラフの表示
    plt.show()


