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
            print(parsed_txt)

            kanji_counter = 0
            kanji_list = []
            kanji_array = []
            lines_counter = 0
            for i, parsed_word in enumerate(parsed_txt):
                  lines_counter += 1
                  print(len(parsed_txt))
                  if i < len(parsed_txt):
                        parsed_word = parsed_word.split('\t')
                        if len(parsed_word) > 12:
                              if '外' in parsed_word[12]:
                                    if not 65 <= ord(parsed_word[0][0]) <= 122 and not 65313 <= ord(parsed_word[0][0]) <= 65338 and not 12450 <= ord(parsed_word[0][0]) <= 12538 and not 12352 <= ord(parsed_word[0][0]) <= 12447 and not 65296 <= ord(parsed_word[0][0]) <= 65305 and not 48 <= ord(parsed_word[0][0]) <= 57 and not parsed_word[0] == '汗': #а как же этикет?!
                                          kanji_counter += 1
                                          kanji_list.append(parsed_word[0])
                                          #print(parsed_word[0])
                              else:
                                    if parsed_word[0] == '《':
                                          i += 1
                                          parsed_word = parsed_txt[i].split('\t')
                                          reading = parsed_word[0]
                                          if 12450 <= ord(parsed_txt[i][0]) <= 12538:
                                                i = i - 2
                                                parsed_word = parsed_txt[i].split('\t')
                                                word = parsed_word[0]
                                                if 65 <= ord(word[0]) <= 122:
                                                      continue
                                                elif 65313 <= ord(word[0]) <= 65338:
                                                      continue
                                                else:
                                                      reading = '*' + reading
                                                      kanji_list.append(reading)
                                                      kanji_counter += 1
                                                      i = i - 1
                                                      parsed_word = parsed_txt[i].split('\t')
                                                      previous_word = parsed_word[0]
                                                      #print(reading)
                                    else:
                                          break

            #print(kanji_list)


