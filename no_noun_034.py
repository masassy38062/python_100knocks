#34. 「AのB」
#2つの名詞が「の」で連結されている名詞句を抽出せよ．
#-*-coding:utf-8-*-

import codecs
import re
import ast
from training.bigram_005 import ngram

if __name__ == "__main__":
    pattern1 = re.compile(r'^名詞助詞名詞$')
    pattern2 = re.compile(r'.*の.*')
    pattern3 = re.compile(r'^の.*')
    pattern4 = re.compile(r'.*の$')

    with codecs.open('neko.txt.mecab.analyze','r','utf-8') as f:
        temp_lines = f.readlines()

#posとsurfaceのデータを取得した基礎データを作成する
    temp_data1 = ''
    temp_data2 = ''
    for temp_line in temp_lines:
        temp_dict = ast.literal_eval(temp_line)
        temp_data1 += temp_dict['pos']+' '
        temp_data2 += temp_dict['surface']+' '


#基礎データをbigram関数で3つずつに区切る
    type='word'
    N = 3
    ngram_data1 = ngram(temp_data1,N,type)
    ngram_data2 = ngram(temp_data2,N,type)
    match_list=[]
#名詞助詞名詞の並びの箇所のindexを抜き出す
    for index,data in enumerate(ngram_data1):
        if(pattern1.match(data)):
             match_list.append(index)
        else:
            continue

#抜き出したindexと同じ番号を持つsurface情報を抜き出し、AのBに当てはまる情報に正規表現でフィルタする
    match_word=[]
    for search_index,search_data in enumerate(ngram_data2):
        if search_index in match_list:
            if pattern2.match(search_data) and not pattern3.match(search_data) and not pattern4.match(search_data):
                match_word.append(search_data)
        else:
            continue

#精査した情報から重複データの削除
    match_data = set(match_word)
#neko.txt.mecab.analyze_034に結果を書き出す
    with codecs.open('neko.txt.mecab.analyze_034','w','utf-8') as wf:
        for write_data in match_data:
            wf.write(str(match_data)+'\n')




