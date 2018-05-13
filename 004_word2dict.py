#04. 元素記号
#"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

def word2dict(msg):
    temp = ''
    temp_msg = ''
    temp_list=[]
    i = 1

    for temp in msg:
        if(temp==' ' or temp=='. '):
            temp_list.append((i, temp_msg))
            temp_msg = ''
            i = i + 1
        else:
            temp_msg+=temp
    temp_list.append((i,temp_msg))
    return  temp_list

if __name__=="__main__":
    msg = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    dic = {}
    temp_list = []
    temp_list = word2dict(msg)
    for key,item in temp_list:
        if(key==1 or key == 5 or key == 6 or key == 7or key == 8or key == 9or key == 15or key == 16or key == 19):
            dic[key]=item[:1]
        else:
            dic[key]=item[:2]
    print(dic)