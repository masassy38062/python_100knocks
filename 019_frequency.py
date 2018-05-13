#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
#確認にはcut, uniq, sortコマンドを用いよ

import codecs
import subprocess
import collections
import operator

def frequency(data):
    cut_temp = []
    sort_temp = []
    count_dict={}

    # cut -f 1の働き
    for temp in data:
        cut_temp.append(temp.split()[:1])

    # sort1の働き
    sort_temp = sorted(cut_temp)

    #listの中の要素数をカウント
    # uniq -cの働き
    count_dict = collections.Counter(map(str,sort_temp))
    for value,count in sorted(count_dict.items(),key=operator.itemgetter(1),reverse=True):
        print(count,str(value).lstrip("['").rstrip("']"))

if __name__=="__main__":
    basepath = './'
    filename = 'hightemp.txt'
    with codecs.open(filename,'r','utf-8') as f:
        frequency(f.readlines())

    cut=subprocess.Popen(["cut","-f","1",basepath+filename],stdout=subprocess.PIPE)
    sort1 = subprocess.Popen(["sort"],stdin=cut.stdout,stdout=subprocess.PIPE)
    uniq = subprocess.Popen(["uniq","-c"],stdin=sort1.stdout,stdout=subprocess.PIPE)
    sort2 = subprocess.Popen(["sort","-r"],stdin=uniq.stdout,stdout=subprocess.PIPE)
    end_of_pipe = sort2.stdout
    print('\nlinuxコマンド:')
    for line in end_of_pipe:
        print(line.decode('utf-8').lstrip(' ').rstrip('\n'))


