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

            parsed_by_words = parsed_txt.split('\n')
            #print(parsed_by_words)

            kanji_list = []
            for i, parsed_word in enumerate(parsed_by_words):
                  if i < len(parsed_by_words):
                        parsed_word = parsed_word.split('\t')
                        if parsed_word[0] == '《':
                              i += 1
                              parsed_word = parsed_by_words[i].split('\t')
                              reading = parsed_word[0]
                              if 12450 <= ord(parsed_by_words[i][0]) <= 12538:
                                    i = i - 2
                                    parsed_word = parsed_by_words[i].split('\t')
                                    word = parsed_word[0]
                                    if 65 <= ord(word[0]) <= 122:
                                          continue
                                    elif 65313 <= ord(word[0]) <= 65338:
                                          continue
                                    else:
                                          kanji_list.append(word)
                                          i = i - 1
                                          parsed_word = parsed_by_words[i].split('\t')
                                          previous_word = parsed_word[0]
                                          print(previous_word, word, reading)


