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
new_data = "予防　接種"
new_data_vec = vectorizer.transform([new_data])

#内容表示
print(new_data_vec)
print(new_data_vec.toarray())

#文書間のユークリッド距離計算 定義
def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

#単語の出現回数ベクトルを正規化
def dist_norm(v1, v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
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
    #d = dist_raw(temp_data_vec, new_data_vec)
    d = dist_norm(temp_data_vec, new_data_vec)
    print("=== Post %i with dist=%.2f: %s" % (i, d, temp_data))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best data is %i with dist=%.2f" % (best_i, best_dist))
