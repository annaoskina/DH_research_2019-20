from pymecab.pymecab import PyMecab

with open('/home/anna/DH_research_2019-20/Source_for_research/bocchan.txt', 'r', encoding = 'Shift-JIS') as f:
    text = f.read()

mecab = PyMecab()

for token in mecab.tokenize(text):
    #print(token.surface, token.pos1)
    print(token.surface, token.pos1, token.pos2, token.pos3, token.pos4)
