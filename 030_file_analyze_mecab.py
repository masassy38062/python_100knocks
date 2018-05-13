#夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
#その結果をneko.txt.mecabというファイルに保存せよ．
# このファイルを用いて，以下の問に対応するプログラムを実装せよ．
#なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

import MeCab
import codecs

def file_analyze_mecab(input_filename,output_filename):

    with codecs.open(input_filename,'r','utf-8') as f:
        text = f.read()

    m = MeCab.Tagger("mecabrc")
    wt = m.parse(text)

    with codecs.open(output_filename,'w','utf-8') as wf:
        wf.write(wt)

if __name__=="__main__":
    file_analyze_mecab('neko.txt','neko.txt.mecab')

