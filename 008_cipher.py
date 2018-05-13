#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ。
#英小文字ならば(219 - 文字コード)の文字に置換。
#その他の文字はそのまま出力。この関数を用い，英語のメッセージを暗号化・復号化せよ

import re

def cipher(msg):
    pattern = re.compile("[a-z]")
    cipher_msg = ''
    for temp in msg:
        if pattern.match(temp):
            cipher_msg += chr(219-ord(temp))
            continue
        else:
            cipher_msg += temp
            continue
    return  cipher_msg

if __name__=="__main__":
    msg = "Cipher_msg_012345"
    print("元msg=",msg)
    c = cipher(msg)
    print("暗号化=",c)
    d = cipher(c)
    print("復号化=",d)

