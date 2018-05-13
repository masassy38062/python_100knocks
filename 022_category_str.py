#22. カテゴリ名の抽出
#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re
import json
import gzip

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

if __name__=="__main__":
    pattern = re.compile(r'.*Category:.*')
    pattern2 = re.compile(r'.*\|.*')
    lines = uk_find()
    for line in lines.split('\n'):
        if pattern.match(line):
            strip_line=line.lstrip("[[Category:").rstrip("]]")
            if pattern2.match(strip_line):
                N = strip_line.find('|')
                strip_line2 = strip_line[:N]
                print(strip_line2)
            else:
                print(strip_line)