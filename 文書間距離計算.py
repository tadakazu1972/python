#�ގ��x�v�Z
#���C�u����
import os
import sys
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer

#���������������t�@�C�����i�[���Ă���f�B���N�g����ݒ�
DIR = "/Users/tadakazu/Desktop/wakati"

#�t�H���_�̒��̕����̃e�L�X�g�t�@�C������C�ɓǍ�
data = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]

#�x�N�g����
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(data)
num_files, num_features = X_train.shape

#��U�A���ʕ\��
print("#Files: %d, #features: %d" % (num_files, num_features))
print(vectorizer.get_feature_names())

#�����f�[�^
new_data = "��� �{ �k�� �n�k �ɂ�� �ЊQ �� ��Q �� �� �� �� �ł� �� �A �ŋ� �� ���� �� �K�p �� �� �܂� �� �H A . �� �� ���e ��� �{ �k�� �� �k�� �� ���� �n�k �� ��� �� �� �� �� �ɂ��� �� �A �\�� �ɂ�� �A �s �� �� ���� �Ȃ� �� �� ���� �ꍇ �� ���� �܂� �B �ڍ� �� �����N �� �� �w ��� �{ �k�� �� �k�� �� ���� �n�k �� ��� �� �� �� �� �ɑ΂��� �s �� �� ���� �Ȃ� �ɂ��� �� �E�B���h�E �� �\�� �� �܂� �x �� �Q�� �� �� �������� �B �y �Ώ� �� �Ȃ� �s �� �z"
new_data_vec = vectorizer.transform([new_data])

#���e�\��
print(new_data_vec)
print(new_data_vec.toarray())

#�����Ԃ̃��[�N���b�h�����v�Z ��`
def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

#�ǂݍ��񂾃t�@�C���S�Čv�Z
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
