#07. テンプレートによる文生成
#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

from string import Template

def template_print(x,y,z):
    value ={'time':x,'name':y,'tempture':z}
    t = Template("$time時の$nameは$tempture")
    return print(t.substitute(value))

if __name__ == "__main__":
    x=12
    y='気温'
    z=22.4
    template_print(x,y,z)
