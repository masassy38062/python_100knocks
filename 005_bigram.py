#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
#この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

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

if __name__ == "__main__":
        msg = "I am an NLPer"
        #msg="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        N=2
#        type='char'
        type='word'
        bigram_list = ngram(msg,N,type)
        print(bigram_list)
