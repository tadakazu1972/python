#�t�H���_���̃e�L�X�g�S�Ă𕪂�����������
#Python 3.6.2
import os
import MeCab

#�t�@�C�����i�[���Ă���f�B���N�g����ݒ�
DIR = "/Users/tadakazu/Desktop/faq"

#�t�H���_�̒��̃t�@�C�����A�f�[�^���i�[
filename = os.listdir(DIR)
data = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]

#���ƂŃt�@�C������ύX���ď����o�������Ƃ��āA�܂��͌��t�@�C������S�R�s�[���Ĕz��m��
filename2 = filename

#�����������ݒ�
mecab = MeCab.Tagger("-Owakati")

#�����������J��Ԃ�
for i in range(len(filename)):
    #���o�p�t�@�C�����@����
    filename2[i] = "wakati_" + filename[i]
    #��������������
    wakati = mecab.parse(data[i])
    #�t�@�C�����ƂƂ��ɕ��������������f�[�^�����o
    with open(filename2[i], "w") as f:
        f.write(wakati)
