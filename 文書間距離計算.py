#類似度計算
#ライブラリ
import os
import sys
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer

#分かち書きしたファイルを格納しているディレクトリを設定
DIR = "/Users/tadakazu/Desktop/wakati"

#フォルダの中の複数のテキストファイルを一気に読込
data = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]

#ベクトル化
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(data)
num_files, num_features = X_train.shape

#一旦、結果表示
print("#Files: %d, #features: %d" % (num_files, num_features))
print(vectorizer.get_feature_names())

#検索データ
new_data = "大阪 府 北部 地震 による 災害 の 被害 を 受け た の です が 、 税金 の 減免 は 適用 さ れ ます か ？ A . ご 回答 内容 大阪 府 北部 を 震源 と する 地震 で 被災 さ れ た 方 について は 、 申請 により 、 市 税 の 減免 など が 受け られる 場合 が あり ます 。 詳細 は リンク 先 の 『 大阪 府 北部 を 震源 と する 地震 で 被災 さ れ た 方 に対する 市 税 の 減免 など について 別 ウィンドウ で 表示 し ます 』 を 参照 し て ください 。 【 対象 と なる 市 税 】"
new_data_vec = vectorizer.transform([new_data])

#内容表示
print(new_data_vec)
print(new_data_vec.toarray())

#文書間のユークリッド距離計算 定義
def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

#読み込んだファイル全て計算
best_doc = None
best_dist = sys.maxsize
best_i = None
for i in range(0, num_files):
    temp_data = data[i]
    if temp_data == new_data:
        continue
    temp_data_vec = X_train.getrow(i)
    d = dist_raw(temp_data_vec, new_data_vec)
    print("=== Post %i with dist=%.2f: %s" % (i, d, temp_data))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best data is %i with dist=%.2f" % (best_i, best_dist))
