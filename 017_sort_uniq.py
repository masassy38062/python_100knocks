#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

#-*-coding:utf-8-*-
import codecs
import subprocess

def sort_uniq(data):
    cut_temp = []
    sort_temp = []
    uniq_temp = []

#cut -f 1の働き
    for temp in data:
        cut_temp.append(temp.split()[:1])

#sortの働き
    sort_temp = sorted(cut_temp)

#uniqの働き
    for temp in sort_temp:
        if temp not in uniq_temp:
            uniq_temp.append(temp)

#listをstrに変換後、余分な文字を削除して表示
    sort_uniq_data = map(str,uniq_temp)
    for temp in sort_uniq_data:
        print(''.join(temp).lstrip("['").rstrip("']"))

if __name__ == "__main__":
    filename = 'hightemp.txt'
    basepath = './'
    f = codecs.open(filename,'r','utf-8')
    sort_uniq(f.readlines())

    cut=subprocess.Popen(["cut","-f","1",basepath+filename],stdout=subprocess.PIPE)
    sort = subprocess.Popen(["sort"],stdin=cut.stdout,stdout=subprocess.PIPE)
    uniq = subprocess.Popen(["uniq"],stdin=sort.stdout,stdout=subprocess.PIPE)
    end_of_pipe = uniq.stdout
    print('\nlinuxコマンド:')
    for line in end_of_pipe:
        print(line.decode('utf-8').rstrip('\n'))
