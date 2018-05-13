#25. テンプレートの抽出
#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ

import json
import gzip
import re

def uk_find():
    basepath = './'
    filename = 'jawiki-country.json.gz'
    pattern = r"イギリス"
    with gzip.open(basepath + filename, 'rt')as gf:
        for line in gf:
            # json.loadsはstr→dict、json.loadはfile→dict
            json_data = json.loads(line)
            if (re.match(json_data['title'], pattern)):
                return json_data['text']

def basic_info_find(lines):
    pattern1 = re.compile(r'^\{\{[redirect|基礎情報].*')
    pattern2 = re.compile(r'^\|.*')
    pattern3 = re.compile(r'^\}\}$')

    basic_dict = {}
    for line in lines.split('\n'):
        if pattern1.match(line):
            continue

        elif pattern2.match(line):
            point = line.find('=')
            MAX = len(line)
            title = line[0:point].lstrip('|').rstrip(' ')
            data = line[point:MAX].lstrip('= ')
            basic_dict.update({title: data})

        elif pattern3.match(line):
            break
    return basic_dict

if __name__=="__main__":
    lines = uk_find()
    basic_dict = basic_info_find(lines)
    for key,value in basic_dict.items():
        print("{"+key+':'+value+"}")

    print("データ数",len(basic_dict.items()))