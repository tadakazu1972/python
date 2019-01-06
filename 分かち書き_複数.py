#フォルダ内のテキスト全てを分かち書き処理
#Python 3.6.2
import os
import MeCab

#ファイルを格納しているディレクトリを設定
DIR = "/Users/tadakazu/Desktop/faq"

#フォルダの中のファイル名、データを格納
filename = os.listdir(DIR)
data = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]

#あとでファイル名を変更して書き出す準備として、まずは元ファイル名を全コピーして配列確保
filename2 = filename

#分かち書き設定
mecab = MeCab.Tagger("-Owakati")

#分かち書き繰り返し
for i in range(len(filename)):
    #書出用ファイル名　生成
    filename2[i] = "wakati_" + filename[i]
    #分かち書き処理
    wakati = mecab.parse(data[i])
    #ファイル名とともに分かち書きしたデータを書出
    with open(filename2[i], "w") as f:
        f.write(wakati)
