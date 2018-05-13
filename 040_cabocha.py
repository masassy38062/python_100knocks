#-*-coding:utf-8-*-

import CaboCha
import codecs

if __name__ == "__main__":
    with codecs.open('neko.txt','r','utf-8') as f :
        temp_lines = f.readlines()

    # c = CaboCha.Parser("");
    c = CaboCha.Parser()

    data = ''
    for temp_line in temp_lines:
        data += temp_line.strip('\n').strip(" ")

    tree = c.parse(data)
    cabocha_data = tree.toString(CaboCha.FORMAT_LATTICE)

    with codecs.open('neko.txt.cabocha','w','utf-8') as wf:
        wf.write(cabocha_data)