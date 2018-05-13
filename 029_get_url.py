#29. 国旗画像のURLを取得する
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

# -*- coding:utf-8-*-

import requests
import urllib.parse
import gzip
import json
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

def image_query(filename):
    url = "https://commons.wikimedia.org/w/api.php?"
    action = "action=query&"
    titles = "titles=File:"+urllib.parse.quote(filename)+"&"
    prop = "prop=imageinfo&"
    iiprop="iiprop=url&"
    format = "format=json"
    parameter = url +action+titles+prop+iiprop+format
    return parameter

def get_request(parameter):
    pattern = re.compile(r".*\"url\".*")
    r = requests.get(parameter)
    data = r.json()
    json_data =json.dumps(data["query"]["pages"]["347935"]["imageinfo"],indent=4)
    for temp in json_data.split('\n'):
        if(pattern.search(temp)):
            url_data = temp.replace(" ","")
        else:
            continue

    return url_data

if __name__=="__main__":
    lines = uk_find()
    basic_dict = basic_info_find(lines)
    parameter=image_query(basic_dict['国旗画像'])
    get_url = get_request(parameter)
    print(get_url)