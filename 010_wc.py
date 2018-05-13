#第2章: UNIXコマンドの基礎
#hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
#以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
#さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．

#-*- coding:utf-8 -*-

import subprocess
import codecs

if __name__=="__main__":
    filename = 'hightemp.txt'
    basepath = './'
    f = codecs.open(filename,'r','utf-8')

#\nの数を数える。配列は0から始まるので、最後に+1
    for index,data in enumerate(f):
        data.split('\n')

    print("ファイル内の行数は",index+1)

# wcコマンドで出力を確認する
    output = subprocess.check_output(["wc","-l",basepath+filename])
    print("wc:"+output.decode('utf-8'))