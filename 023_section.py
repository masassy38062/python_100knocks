#23. セクション構造
#記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

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


if __name__=="__main__":
    pattern = re.compile(r'^=.*')
    pattern2 = re.compile(r'^={2}')
    pattern3 = re.compile(r'^={3}')
    pattern4 = re.compile(r'^={4}')

    lines=uk_find()
    for line in lines.split('\n'):
        if pattern.match(line):
            if pattern4.match(line):
                print(line.lstrip('====').rstrip('====')+':レベル4')
            elif pattern3.match(line):
                print(line.lstrip('===').rstrip('===')+':レベル3')
            elif pattern2.match(line):
                print(line.lstrip('==').rstrip('==')+':レベル2')
            else:
                print('no match')