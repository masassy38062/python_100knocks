#09. Typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（"I couldn't believe that I could actually understand what I was reading :
# the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

def word2list(msg):
    temp_msg = ''
    list = []
    for temp in msg:
        temp=temp.rstrip(",.")
        if(temp==' '):
            list.append(temp_msg)
            temp_msg=''
        else:
            temp_msg += temp

    list.append(temp_msg)
    return list

#文字列をランダム化する関数
#random_msgを返す
def random_word(word):
    random_msg=''
    for temp in word:
#4文字以下は処理しない
        if(len(temp)<=4):
            random_msg += temp
            random_msg += " "
            continue
        else:
#文字列の最初はfirst_strに格納
#文字列の最初はlast_strに格納
            temp_length = len(temp)
            first_str= temp[0]
            last_str=temp[temp_length-1]
            random_word_list=[]
            random_word=''
            temp_random_list = []
#取得した文字列の最初と最後は処理しない
#中間の文字列をリスト化してrandom_word_listに入れる
            for index,temp_word in enumerate(temp):
                if(index==0 or index==temp_length-1):
                    continue
                else:
                    random_word_list.append(temp_word)
                continue
#リスト化した文字列からランダムに抽出し、temp_random_listに入れる
#抽出した文字列は抽出元のリストから削除する
            for i in range(len(random_word_list)):
                temp_random_list.append(random.choice(random_word_list))
                random_word_list.remove(temp_random_list[i])
                continue
#ランダムリストをtemp_wordに追加していく
            for temp_word in temp_random_list:
                random_word+=temp_word
                continue
#firstとrandomとlastを組み合わせてrandom_msgへ入れる
            random_msg += (first_str + random_word + last_str)
            random_msg += " "

    return  random_msg

if __name__ == "__main__":
    msg = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    word = word2list(msg)
    random = random_word(word)
    print(random)
