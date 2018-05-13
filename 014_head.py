#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

#-*- coding:utf-8 -*-

import codecs
import subprocess

def head(data,N):
    i=0
    j=0
    msg=''
    while(i<N):
        for temp in data[j]:
            if(temp!='\n'):
                msg += temp
                j+=1
            else:
                msg += '\n'
                i+=1
                j+=1
                break
    else:
        return msg

if __name__=="__main__":
    filename = 'hightemp.txt'
    basepath = './'
    f = codecs.open(filename,'r','utf-8')
    r=f.read()
    N=10
    msg = head(r,N)
    print(msg)

#headコマンドで確認
    output=subprocess.check_output(["head","-n",str(N),basepath+filename])
    print("linuxコマンド:")
    print(output.decode('utf-8'))