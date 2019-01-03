#日本語テキストを分かち書き
#Python 3.6.2

#元テキスト読込(デスクトップに置く)
filename = "/Users/tadakazu/Desktop/sample.txt"
text = open(filename).read()

#分かち書き
#ターミナルでカレントをDesktopに変更しておくのが吉（あとでファイルを取り出しやすい）
import MeCab
mecab = MeCab.Tagger("-Owakati")
wakati = mecab.parse(text)
filename2 = "sample_wakati.txt"
with open(filename2, "w") as f:
    f.write(wakati)
