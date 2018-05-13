#24. ファイル参照の抽出
#記事から参照されているメディアファイルをすべて抜き出せ．

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
    pattern = re.compile(r".*(ファイル|File).*")
    pattern2 = re.compile(r"^|.*")
    lines = uk_find()
    for line in lines.split('\n'):
        if pattern2.search(line):
            line = line.lstrip('|')
        if pattern.search(line):
            start = line.find(':')+1
            end = line.find('|')
            print(line[start:end])