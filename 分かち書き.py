#���{��e�L�X�g�𕪂�������
#Python 3.6.2

#���e�L�X�g�Ǎ�(�f�X�N�g�b�v�ɒu��)
filename = "/Users/tadakazu/Desktop/sample.txt"
text = open(filename).read()

#����������
#�^�[�~�i���ŃJ�����g��Desktop�ɕύX���Ă����̂��g�i���ƂŃt�@�C�������o���₷���j
import MeCab
mecab = MeCab.Tagger("-Owakati")
wakati = mecab.parse(text)
filename2 = "sample_wakati.txt"
with open(filename2, "w") as f:
    f.write(wakati)
