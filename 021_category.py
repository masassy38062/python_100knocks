#21. カテゴリ名を含む行を抽出
#記事中でカテゴリ名を宣言している行を抽出せよ．

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
    pattern = re.compile(r'.*Category.*')
    lines = uk_find()
    for line in lines.split('\n'):
        if pattern.match(line):
            print(line)