#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
#確認にはcutコマンドを用いよ．

# -*- coding:utf-8 -*-

import codecs
import subprocess

if __name__ == "__main__":
    filename = 'hightemp.txt'
    writename1='col1.txt'
    writename2='col2.txt'
    basepath = './'
    f = codecs.open(filename,'r','utf-8')
    r = f.readlines()
    word_list1= []
    word_list2= []

#splitで\t毎に分けてリストに追加する
    for temp1 in r:
        word_list1.append(temp1.split('\t')[0])
    f.close
    f = codecs.open(writename1,'w','utf-8')
    for word in word_list1:
        f.write(word+'\n')
    f.close

    for temp2 in r:
        word_list2.append(temp2.split('\t')[1])
    f.close
    f = codecs.open(writename2,'w','utf-8')
    for word in word_list2:
        f.write(word+'\n')
    f.close

#cutコマンドで出力を確認する
    output = subprocess.check_output(["cut","-f","1,2",basepath+filename])
    print(output.decode('utf-8'))