#30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
#ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとする
#マッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
#第4章の残りの問題では，ここで作ったプログラムを活用せよ．

#-*-coding:utf-8-*-

import codecs

if __name__ == "__main__":
    with codecs.open("neko.txt.mecab",'r','utf-8') as f:
        data = f.readlines()

    mecab_list=[]
    temp_dict ={}
    for temp_word in data:
        temp_word = temp_word.replace('\t', ',')
        temp_word = temp_word.replace('\n', '')
        if(temp_word.count(',')==9 or temp_word.count(',')==7):
            temp_list = temp_word.split(',')
            temp_dict={'surface':temp_list[0],'base':temp_list[7],'pos':temp_list[1],'pos1':temp_list[2]}
            mecab_list.append(temp_dict)
            print(temp_dict)
        else:
            continue

    with codecs.open('neko.txt.mecab.analyze','w','utf-8') as wf:
        for line in mecab_list:
            wf.write(str(line)+'\n')

