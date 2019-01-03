#�ގ��x�v�Z
#���C�u����
import os
from sklearn.feature_extraction.text import CountVectorizer

#���������������t�@�C�����i�[���Ă���f�B���N�g����ݒ�
DIR = "/Users/tadakazu/Desktop/text"

#�t�H���_�̒��̕����̃e�L�X�g�t�@�C������C�ɓǍ�
data = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]

#�x�N�g����
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(data)
num_files, num_features = X_train.shape

#��U�A���ʕ\��
print("#Files: %d, #features: %d" % (num_files, num_features))
print(vectorizer.get_feature_names())

#���ƂŎg��
new_data = "imaging databases"
new_data_vec = vectorizer.transform([new_data])

#���e�\��
print(new_data_vec)
print(new_data_vec.toarray())

#�����Ԃ̃��[�N���b�h�����v�Z ��`
import scipy as sp
def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

#�ǂݍ��񂾃t�@�C���S�Čv�Z
import sys
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
