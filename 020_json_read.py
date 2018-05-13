#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
#問題21-29では，ここで抽出した記事本文に対して実行せよ．

#-*- coding:utf-8 -*-

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

if __name__ == "__main__":
    json_data = uk_find()
    print(json_data)
    print(len(json_data.split('\n')))