#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
#タブ区切りで並べたテキストファイルを作成せよ．
#確認にはpasteコマンドを用いよ．

#-*- conding:utf-8 -*-

import codecs
import subprocess
basepath = './'
filename1 = 'col1.txt'
filename2 = 'col2.txt'
filename3 = 'col3.txt'

#readlinesでファイルを読み込みリスト化
f1 = codecs.open(filename1,'r','utf-8')
r1 = f1.readlines()
f1.close()

f2 = codecs.open(filename2,'r','utf-8')
r2 = f2.readlines()
f2.close()

s_r1=''
s_r2=''

#リストを文字列に変更し、r1の\nは\tに変更(\tが番兵になる)
for data in r1:
    s_r1 += str(data)
    s_r1=s_r1.replace('\n','\t')

#リストを文字列に変更(\nは番兵のためそのまま残す)
for data in r2:
    s_r2 += str(data)

address=''
i=0
#s_r1を1文字ずつ評価し、番兵(\t)がくるまでaddressにデータを追加
for temp in s_r1:
    if(temp!='\t'):
        address+=temp
    else:
# addressにs_r2のデータを番兵(\n)がくるまで追加
        address+='\t'
        while(s_r2[i]!='\n'):
            address+=s_r2[i]
            i+=1
        else:
            address+='\n'
            i+=1
            continue

f3=codecs.open(filename3,'w','utf-8')
f3.write(address)
f3.close()

output=subprocess.check_output(["paste",basepath+filename1,basepath+filename2])
print("linuxコマンド:")
print(output.decode('utf-8'))
