#03. 円周率
#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解
#各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
# -*- coding: utf-8 -*-

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


if __name__ == "__main__":
    msg = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    list = []
    num_list = []

    list = word2list(msg)
    for num in list:
            num_list.append(len(num))
    print(num_list)
