#18. 各行を3コラム目の数値の降順にソート
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
#確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．


import codecs
import subprocess
import operator

def r_sort(data):
    cut_temp = []
    sort_temp = []

# cut -f 2-3の働き
    for temp in data:
        cut_temp.append(temp.split())

# sortの働き
    sort_temp = sorted(cut_temp,key=operator.itemgetter(2),reverse=True)

# listをstrに変換後、余分な文字を削除して表示
    sort_data = map(str, sort_temp)
    for temp in sort_data:
        print(''.join(temp).lstrip("['").rstrip("']"))

if __name__=="__main__":
    basepath = './'
    filename = 'hightemp.txt'
    with codecs.open(filename,'r','utf-8') as f:
        r_sort(f.readlines())

    sort= subprocess.check_output(["sort","-r","-k","3",basepath+filename])
    print('\nlinuxコマンド:')
    print(sort.decode('utf-8'))
