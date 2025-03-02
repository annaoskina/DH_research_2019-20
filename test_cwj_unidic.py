import re
import MeCab
import csv
import os
import matplotlib.pyplot as plt

def open_file(path, filename):
      with open('/home/anna/DH_research_2019-20/Source_for_research/{}'.format(filename), 'r', encoding = 'Shift-JIS') as f:
            print('\n', filename)
            raw_file = f.read()
      return raw_file

def clean_the_text(raw_file):
      step_1 = re.sub('(----------).+(---------)', '', raw_file, flags=re.DOTALL)
      step_2 = re.sub('［＃.+?］', '', step_1)
      clean_txt = re.sub('(底本：「).+?(ボランティアの皆さんです。)', '', step_2, flags=re.DOTALL)
      return clean_txt

def parse_with_cwj(clean_txt):
      m = MeCab.Tagger('-d /home/anna/Documents/unidic-cwj-2.3.0')
      parsed_txt = m.parse(clean_txt)
      parsed_txt = parsed_txt.replace(',', '\t')
      #parsed_by_words = parsed_txt.split('\n')
      return parsed_txt #один список разобранных слов

def count_katakana(parsed_txt):
      parsed_txt = parsed_txt.split('\n')
      katakana_counter = 0
      katakana_list = []
      #hiragana_list = []
      katakana_array = []
      for i, token in enumerate(parsed_txt):
            if i < len(parsed_txt):
                  token = token.split('\t')
                  if len(token) > 13:
                        if '外' in token[13]:
                              if 12450 <= ord(token[0][0]) <= 12538: #включаю катакану
                                    if i:
                                          if parsed_txt[i-1][0] == '《':
                                                continue
                                          else:
                                                katakana_counter += 1
                                                katakana_list.append(token[0])
                                    else:
                                          katakana_counter += 1
                                          katakana_list.append(token[0])
                        elif '固' in token[13]:
                              if 12450 <= ord(token[0][0]) <= 12538: #включаю катакану
                                    if i:
                                          if parsed_txt[i-1][0] == '《':
                                                continue
                                          else:
                                                katakana_counter += 1
                                                katakana_list.append(token[0])
                                    else:
                                          katakana_counter += 1
                                          katakana_list.append(token[0])
                  if(len(parsed_txt) % 5000 == 0):
                        katakana_array.append(katakana_counter)
                        katakana_counter = 0
      katakana_array.append(katakana_counter)
      print(katakana_list)
      print(len(katakana_list))
      return katakana_array

def count_romaji(parsed_txt):
      parsed_txt = parsed_txt.split('\n')
      romaji_counter = 0
      romaji_list = []
      romaji_array = []
      for token in parsed_txt:
            token = token.split('\t')
            if len(token) > 13:
                  if '外' in token[13]:
                        if 65 <= ord(token[0][0]) <= 122: #включаю латиницу half-width (H)
                              romaji_counter += 1
                              romaji_list.append(token[0])
                        if 65313 <= ord(token[0][0]) <= 65338: #включаю латиницу full-width (Ｈ)
                              romaji_counter += 1
                              romaji_list.append(token[0])
                  elif '固' in token[13]:
                        if 65 <= ord(token[0][0]) <= 122:
                              romaji_counter += 1
                              romaji_list.append(token[0])
                        if 65313 <= ord(token[0][0]) <= 65338: #включаю латиницу full-width (Ｈ)
                              romaji_counter += 1
                              romaji_list.append(token[0])
            if 1 < len(token) <= 7: 
                  if 65 <= ord(token[0][0]) <= 122:
                        romaji_counter += 1
                        romaji_list.append(token[0])
                  if 65313 <= ord(token[0][0]) <= 65338: #включаю латиницу full-width (Ｈ)
                        romaji_counter += 1
                        romaji_list.append(token[0])
            if(len(parsed_txt) % 5000 == 0):
                  romaji_array.append(romaji_counter)
                  romaji_counter = 0
      romaji_array.append(romaji_counter)
      print(romaji_list)
      print(len(romaji_list))
      return romaji_array

def count_kanji(parsed_txt):
      parsed_txt = parsed_txt.split('\n')
      kanji_counter = 0
      kanji_list = []
      kanji_array = []
      for i, token in enumerate(parsed_txt):
            if i < len(parsed_txt):
                  token = token.split('\t') #token - это список (слово + разбор)
                  if len(token) > 13:
                        if '外' in token[13]:
                              if not 65 <= ord(token[0][0]) <= 122 and not 65313 <= ord(token[0][0]) <= 65338 and not 12450 <= ord(token[0][0]) <= 12538 and not 12352 <= ord(token[0][0]) <= 12447 and not 65296 <= ord(token[0][0]) <= 65305 and not 48 <= ord(token[0][0]) <= 57: #а как же этикет?!
                                    kanji_counter += 1
                                    kanji_list.append(token[0])
                        else:
                              if token[0] == '《':
                                    new_token = parsed_txt[i+1].split('\t')
                                    furigana = new_token[0]
                                    if 12450 <= ord(furigana[0]) <= 12538: #если первый символ - это катакана
                                          maybe_kanji_token = parsed_txt[i-1].split('\t')
                                          if len(maybe_kanji_token) > 13:
                                                if not 65 <= ord(maybe_kanji_token[0][0]) <= 122\
                                                   and not 65313 <= ord(maybe_kanji_token[0][0]) <= 65338\
                                                   and '外' not in maybe_kanji_token[13]:
                                                      maybe_kanji_token = parsed_txt[i-2].split('\t')
                                                      if len(maybe_kanji_token) > 13:
                                                            if '外' not in maybe_kanji_token[13]:
                                                                  furigana = '*' + furigana
                                                                  kanji_counter += 1
                                                                  kanji_list.append(furigana)
                                                                  #print(furigana)
                              else:
                                    continue
            if(len(parsed_txt) % 5000 == 0):
                  kanji_array.append(kanji_counter)
                  kanji_counter = 0
      kanji_array.append(kanji_counter)
      print(kanji_list)
      print(len(kanji_list))
      return kanji_array

def write_result_tsv (filename, parsed_txt):
      with open('/home/anna/DH_research_2019-20/Files_tsv_kindai/{}.tsv'.format(filename), 'w', encoding = 'utf-8') as fw:
            fw.write("{}".format(parsed_txt))

def visualization(result, filename):
      plt.plot(result[0], 'g', label='katakana', linewidth=3)
      #print('result[0] = ', result[0])
      plt.plot(result[1], 'b', label='kanji', linewidth=3)
      #print('result[1] = ', result[1])
      plt.plot(result[2], 'red', label='romaji', linewidth=3)
      #print('result[2] = ', result[2])
      plt.title(filename)
      plt.savefig('/home/anna/DH_research_2019-20/Results_plot/{}.png'.format(filename))
      #plt.show()

def main():
      path = '/home/anna/DH_research_2019-20/Source_for_research'
      files = os.listdir(path)
      for filename in files:
            if not filename.endswith('.txt'):
                  continue
            raw_file = open_file(path, filename)
            clean_txt = clean_the_text(raw_file)
            parsed_txt = parse_with_cwj(clean_txt)
            #write_result_tsv(filename, parsed_txt)
            count_katakana(parsed_txt)
            #count_romaji(parsed_txt)
            #count_kanji(parsed_txt)
            
if __name__ == '__main__':
      main()
