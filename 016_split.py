#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，
#入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ

import codecs
import subprocess
import math

def split(data,N):
    index=0
#書き出すファイル数を計算する
    page=math.ceil(len(data)/N)
    for i in range(0,page):
#リストを文字列にして書き出すデータをwrite_dataに追記
        write_data=''.join(data[index:N+index])
        index+=N
        f=codecs.open('write_data'+str(index),'w','utf-8')
        f.write(write_data)

if __name__ == "__main__":
    filename = 'hightemp.txt'
    basepath = './'
    N = 15
    f=codecs.open(filename,'r','utf-8')
    split(f.readlines(),N)

    subprocess.check_output(["split","-l",str(N),basepath+filename,"cmd_"+str(N)])
