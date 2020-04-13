import re
import MeCab

with open('/home/anna/DH_research_2019-20/Source_for_research/buncho.txt', 'r', encoding = 'Shift-JIS') as f:
    text = f.read()

step_1 = re.sub('(----------).+(---------)', '', text, flags=re.DOTALL) #очищаю от условных обозначений в начале
step_2 = re.sub('［＃.+?］', '', step_1)
clean_txt = re.sub('(底本：「).+?(ボランティアの皆さんです。)', '', step_2, flags=re.DOTALL) #очищаю от метаданных

m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
parsed_txt = m.parse(clean_txt)
parsed_txt = parsed_txt.replace(',', '\t')

parsed_by_words = parsed_txt.split('\n')
for tokens in parsed_by_words:
      tokens = tokens.split('\t')
      #print(tokens)
      
#['洋灯', '名詞', '普通名詞', '一般', '*', '*', '*', 'ヨウトウ', '洋灯', '洋灯', 'ヨートー', 'ヨウトウ', '漢', '洋灯', 'ヨートー', 'ヨウトウ', 'ヨウトウ', '*', '*', '*', '*', '*', '*', '0', 'C2', '*']
#['《', '補助記号', '括弧開', '*', '*', '*', '*', '', '《', '《', '', '', '記号', '《', '', '', '', '*', '*', '*', '*', '*', '*', '*', '*', '*']
#['ランプ', '名詞', '普通名詞', '一般', '*', '*', '*', 'ランプ', 'ランプ-lamp', 'ランプ', 'ランプ', 'ランプ', '外', 'ランプ', 'ランプ', 'ランプ', 'ランプ', '*', '*', '*', '*', '*', '*', '1', 'C1', '*']

      kanji_list = []
      for i, token in enumerate(tokens):
            if token == '《':
                  i += 1
                  if 12450 <= ord(tokens[i][0]) <= 12538:   #проверяю, является ли знак катаканой IndexError: string index out of range
                        i = i - 2                           #возвращаюсь к предыдущему токену
                        kanji_list.append(token[i])         #записываю его в список иероглифов

print(kanji_list)

            
