import re
import MeCab
import os

files = os.listdir('/home/anna/DH_research_2019-20/Source_for_research')
for filename in files:
      if not filename.endswith('.txt'):
            continue
      with open('/home/anna/DH_research_2019-20/Source_for_research/{}'.format(filename), 'r', encoding = 'Shift-JIS') as f:
            print('\n', filename)
            text = f.read()
            step_1 = re.sub('(----------).+(---------)', '', text, flags=re.DOTALL) #очищаю от условных обозначений в начале
            step_2 = re.sub('［＃.+?］', '', step_1)
            clean_txt = re.sub('(底本：「).+?(ボランティアの皆さんです。)', '', step_2, flags=re.DOTALL) #очищаю от метаданных

            m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
            parsed_txt = m.parse(clean_txt)
            parsed_txt = parsed_txt.replace(',', '\t')
            parsed_txt = parsed_txt.split('\n')
            #print(parsed_txt)

            katakana_counter = 0
            katakana_list = []
            katakana_array = []
            lines_counter = 0
            for i, token in enumerate(parsed_txt):
                  lines_counter += 1
                  if i < len(parsed_txt):
                        token = token.split('\t')
                        if len(token) > 12:
                              if token[12] == '外':
                                    if 12450 <= ord(token[0][0]) <= 12538: #включаю катакану
                                          if parsed_txt[i-1] == '《':
                                                continue
                                          else:
                                                katakana_counter += 1
                                                katakana_list.append(token[0])
                              if token[12] ==  '固':
                                    if 12450 <= ord(token[0][0]) <= 12538:
                                          katakana_counter += 1
                                          katakana_list.append(token[0])
            print(katakana_list)
                                          

