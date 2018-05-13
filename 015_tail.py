#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import codecs
import subprocess

def tail(data,N):
    max = len(data)
    print(''.join(data[max-N:]))

if __name__=="__main__":
    filename = 'hightemp.txt'
    basepath = './'
    f = codecs.open(filename,'r','utf-8')
    N=3
    tail(f.readlines(),N)

#tailコマンドで確認
    output=subprocess.check_output(["tail","-n",str(N),basepath+filename])
    print("linuxコマンド:")
    print(output.decode('utf-8'))