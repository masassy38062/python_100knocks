#-*-coding:utf-8-*-

import CaboCha

if __name__ == "__main__":
    c = CaboCha.Parser()
    sentence = "太郎はこの本を二郎を見た女性に渡した。"
    print(c.parseToString(sentence))