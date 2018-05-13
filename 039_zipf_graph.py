#39. Zipfの法則
#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

import codecs
import ast
import collections
import operator
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#-*-coding:utf-8-*-

if __name__ == "__main__":
    with codecs.open('neko.txt.mecab.analyze','r','utf-8') as f:
        temp_lines = f.readlines()

    temp_list = []
    temp_word = ''
    temp_dict = {}

    for temp_line in temp_lines:
        temp_dict = ast.literal_eval(temp_line)
        temp_word = temp_dict['surface']
        temp_list.append(temp_word)

    count_dict = {}
    count_dict = collections.Counter(map(str,temp_list))

    graph_x_list = []
    graph_y_list = []
    for key,value in sorted(count_dict.items(),key=operator.itemgetter(1),reverse=True):
        graph_x_list.append(key)
        graph_y_list.append(value)

#日本語の設定
    fp = FontProperties(fname=r'/Library/fonts/ipag.ttf', size=11)

#グラフのパラメータ
    plt.title("39.zipfの法則", fontproperties=fp)
    plt.xlabel('出現度順位', fontproperties=fp)
    plt.ylabel('出現頻度', fontproperties=fp)

#x/y軸を対数へ変更
    plt.xscale('log')
    plt.yscale('log')

#x軸
    x = range(1,len(graph_x_list)+1)
    y = graph_y_list

#matplotlib.pyplot.scatter(x,y=x,yはグラフに出力するデータ)
    plt.scatter(x,y)

#グラフの表示
    plt.show()
