#28. MediaWikiマークアップの除去
#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
#国の基本情報を整形せよ．

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

def emphasize_remove(basic_dict):
    remove_dict={}
    pattern = re.compile(r".*'{2,4}.*")
    for key,value in basic_dict.items():
        if pattern.match(value):
            value = value.replace("\'",'')
            remove_dict.update({key:value})
    return remove_dict

def link_remove(emphasize_remove_dict):
    pattern = re.compile(r".*\[{2}.*")
    for key,value in emphasize_remove_dict.items():
        if pattern.match(value):
            value = value.replace('[[','').replace(']]','')
            emphasize_remove_dict.update({key: value})
    return emphasize_remove_dict

#poundを除去する関数。
def pound_check(value):
    pattern = re.compile(r".*pound.*")
    if pattern.match(value):
        value = value.replace("(&pound;)",'')
        return value
    else:
        return  value

#brタグを除去する関数。
def br_check(value):
    pattern1 = re.compile(r".*<br.*")
    if pattern1.match(value):
        value = value.replace("<br />", '').replace("<br/>", '')
        return value
    else:
        return value

#refタグとreference記述を除去する関数。
def ref_check(value):
    pattern2 = re.compile(r".*<ref.*")
    if pattern2.match(value):
        start_point = value.find("<ref")
        value = value[0:start_point]
        return value
    else:
        return value

#{{と}}を除去する関数。
def brackets_check(value):
    pattern3 = re.compile(r".*\{\{.*")
    if pattern3.match(value):
        value = value.replace("{{","").replace("}}","")
        #lang|en|United〜とした場合に最初のパイプから4文字以降を取得#
        start_point = value.find("|")+4
        value = value[start_point:len(value)]
        return value
    else:
        return value

#ファイル：除去する関数。
def file_check(value):
    pattern4 = re.compile(r".*ファイル.*")
    if pattern4.match(value):
        value = value.replace('ファイル:','')
        start_point = value.find("|")
        value = value[0:start_point]
        return value
    else:
        return value

#小文字の|を除去する関数。|のみと|+()が存在するパターンを除去。
def pipe_check(value):
     pattern5 = re.compile(r".*\|.*")
     pattern6 = re.compile(r".*\(.*")
     if pattern5.match(value) and pattern6.match(value) :
         end_point = value.find("|")
         value = value[0:end_point] + ")"
         return value
     elif pattern5.match(value):
         end_point = value.find("|")
         value = value[0:end_point]
         return value
     else:
         return value

#大文字の（を除去する関数
def other_check(value):
    pattern7 = re.compile(r"^\（")
    if pattern7.match(value):
        value = value.replace("（","")
        return value
    else:
        return value


def markup_remove(link_remove_dict):
    for key,value in link_remove_dict.items():
        value = pound_check(value)
        value = br_check(value)
        value = ref_check(value)
        value = brackets_check(value)
        value = file_check(value)
        value = pipe_check(value)
        value = other_check(value)
        link_remove_dict.update({key:value})

    return link_remove_dict


if __name__=="__main__":
    lines = uk_find()
    basic_dict = basic_info_find(lines)
    emphasize_remove_dict=emphasize_remove(basic_dict)
    link_remove_dict = link_remove(emphasize_remove_dict)
    markup_remove_dict = markup_remove(link_remove_dict)

    for key,value in markup_remove_dict.items():
        print(key+':'+value)

    print(len(markup_remove_dict.items()))