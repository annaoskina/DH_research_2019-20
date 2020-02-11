from pymecab.pymecab import PyMecab


text = 'テクノロジーで「ビジネスとジャーナリズムの両立」を実現する'

mecab = PyMecab()

for token in mecab.tokenize(text):
    print(token.surface, token.pos1)