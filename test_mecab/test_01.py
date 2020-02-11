# -- coding UTF-8 --

import PyMecab
#from natto import MeCab

text = '「内陣には御主《おんあるじ》耶蘇《ヤソ》基督《キリスト》の画像《ぐわざう》の前に、燐寸'

#mecab = PyMecab(options='--dicdir=C:\\Python38\\UniDic-MLJ\\ --rcfile=C:\\Python38\\UniDic-MLJ\\dicrc')

mecab = PyMecab()


for token in mecab.tokenize(text):
    # additional_entries', 'base_form', 'conjugation_form', 'conjugation_type', 'count', 'index', 'pos1', 'pos2', 'pos3', 'pos4', 'pronunciation', 'reading', 'surface'
    print(token.surface, token.pos1, token.base_form, token.pos4)

