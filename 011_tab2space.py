#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

#-*- coding:utf-8 -*-

import subprocess
import codecs

if __name__=="__main__":
    filename = 'hightemp.txt'
    basepath = './'
    f = codecs.open(filename,'r','utf-8')
#readは1字、readlineは1行、readlinesは全ての行を読む
    r = f.read()
    space_data=''
    for tab_data in r:
        if(tab_data=='\t'):
            space_data += " "
            continue
        else:
            space_data += tab_data

    print(space_data)
# sedコマンドで出力を確認する
    output =subprocess.check_output(["sed","-e" ,"s/\t/ /g",basepath+filename])
    print("linuxコマンド:")
    print(output.decode('utf-8'))
