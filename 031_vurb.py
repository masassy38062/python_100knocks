#31. 動詞
#動詞の表層形をすべて抽出せよ．
#-*-coding:utf-8-*-

import codecs
import re
import ast

if __name__ == "__main__":
    with codecs.open("neko.txt.mecab.analyze",'r','utf-8') as f:
        temp_lines = f.readlines()

    pattern = re.compile(r".*動詞.*")
    data = {}
    for temp_line in temp_lines:
        if pattern.match(temp_line):
            data = ast.literal_eval(temp_line)
            print(data['surface'])
        else:
            continue
