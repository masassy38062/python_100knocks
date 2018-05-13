#06. 集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

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

def ngram(msg,N,type):
    if(type=='word'):
        bigram_word=''
        bigram_list=[]
        temp_list=word2list(msg)
        i=0
        while(i < int(len(temp_list))-1):
            word_list = temp_list[i:(N+i)]
            for word in word_list:
                bigram_word += word
                continue
            bigram_list.append(bigram_word)
            bigram_word =''
            i +=1
        return bigram_list

    elif(type=='char'):
        temp_char_list=[]
        temp_bigram_list=[]
        bigram_char = ''
        bigram_list = []
        for temp_char in msg:
            if(temp_char==' ' or temp_char==','):
                continue
            else:
                temp_char_list.append(temp_char)
            continue
        i=0
        while(i<int(len(temp_char_list))-1):
            temp_bigram_list=temp_char_list[i:(N+i)]
            for char in temp_bigram_list:
                bigram_char += char
                continue
            bigram_list.append(bigram_char)
            bigram_char=''
            i+=1
            continue
        return bigram_list

msg1 = "paraparaparadise"
msg2 = "paragraph"
msg3 = "se"

type = 'char'
msg1_list = ngram(msg1,2,type)
msg2_list = ngram(msg2,2,type)
msg3_list = ngram(msg3,2,type)

set_msg1=set(msg1_list)
set_msg2=set(msg2_list)
set_msg3=set(msg3_list)

plus_list = set_msg1 | set_msg2
multi_list = set_msg1 & set_msg2
sub_list = set_msg1 - set_msg2

#multi_list = set(msg1_list) & set(msg2_list)
#multi_list = [msg1_list]and[msg2_list]

print("msg1_list=",msg1_list)
print("msg2_list=",msg2_list)
print("set_msg1=",set_msg1)
print("set_msg2=",set_msg2)
print("plus_list=",plus_list)
print("multi_list=",multi_list)
print("sub_list=",sub_list)
print("seをset_msg1に含んでいる場合はtrue",set_msg1.issuperset(set_msg3))
print("seをset_msg2に含んでいる場合はtrue",set_msg2.issuperset(set_msg3))
