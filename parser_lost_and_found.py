import re
import MeCab
import csv
import os
import matplotlib.pyplot as plt

def open_file(path, filename):
      with open('/home/anna/DH_research_2019-20/Source_test/{}'.format(filename), 'r', encoding = 'Shift-JIS') as f:
            print('\n', filename)
            raw_file = f.read()
      return raw_file

def clean_the_text(raw_file):
      step_1 = re.sub('(----------).+(---------)', '', raw_file, flags=re.DOTALL)
      step_2 = re.sub('［＃.+?］', '', step_1)
      clean_txt = re.sub('(底本：「).+?(ボランティアの皆さんです。)', '', step_2, flags=re.DOTALL)
      return clean_txt

def parse_the_text(clean_txt):
      m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
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
      lines_counter = 0
      for i, token in enumerate(parsed_txt):
            lines_counter += 1
            if i < len(parsed_txt):
                  token = token.split('\t')
                  if len(token) > 12:
                        if token[12] == '外':
                              if 12450 <= ord(token[0][0]) <= 12538: #включаю катакану
                                    if i < 1:
                                          continue
                                    if parsed_txt[i-1][0] == '《':
                                          continue
                                    else:
                                          katakana_counter += 1
                                          katakana_list.append(token[0])
                        if token[12] ==  '固':
                              if 12450 <= ord(token[0][0]) <= 12538:
                                    katakana_counter += 1
                                    katakana_list.append(token[0])
                  if 1 < len(token) <= 7: #здесь попадается мусор, и я не знаю, как от него избавиться
                        if 12450 <= ord(token[0][0]) <= 12538:
                              katakana_counter += 1
                              katakana_list.append(token[0])
                  if(lines_counter % 5000 == 0):
                        katakana_array.append(katakana_counter)
                        katakana_counter = 0
      katakana_array.append(katakana_counter)
      print(katakana_list)
      print(len(katakana_list))
      #print(hiragana_list)
      return katakana_array

def count_romaji(parsed_txt):
      parsed_txt = parsed_txt.split('\n')
      romaji_counter = 0
      romaji_list = []
      romaji_array = []
      lines_counter = 0
      for token in parsed_txt:
            lines_counter += 1
            token = token.split('\t')
            if len(token) > 12:
                  if token[12] == '外':
                        if 65 <= ord(token[0][0]) <= 122: #включаю латиницу half-width (H)
                              romaji_counter += 1
                              romaji_list.append(token[0])
                        if 65313 <= ord(token[0][0]) <= 65338: #включаю латиницу full-width (Ｈ)
                              romaji_counter += 1
                              romaji_list.append(token[0])
                  if token[12] == '固':
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
            if(lines_counter % 5000 == 0):
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
      lines_counter = 0
      for i, token in enumerate(parsed_txt):
            lines_counter += 1
            if i < len(parsed_txt):
                  token = token.split('\t') #token - это список (слово + разбор)
                  if len(token) > 12:
                        if token[12] == '外':
                              if not 65 <= ord(token[0][0]) <= 122 and not 65313 <= ord(token[0][0]) <= 65338 and not 12450 <= ord(token[0][0]) <= 12538 and not 12352 <= ord(token[0][0]) <= 12447 and not 65296 <= ord(token[0][0]) <= 65305 and not 48 <= ord(token[0][0]) <= 57 and not token[0] == '汗': #а как же этикет?!
                                    kanji_counter += 1
                                    kanji_list.append(token[0])
                                    #print(token[0], token[12])
                        else:
                              if token[0] == '《':
                                    i += 1
                                    if 12450 <= ord(parsed_txt[i][0]) <= 12538:
                                          new_token = parsed_txt[i].split('\t')
                                          reading = new_token[0]
                                          i = i - 2
                                          if 65 <= ord(parsed_txt[i][0]) <= 122:
                                                continue
                                          elif 65313 <= ord(parsed_txt[i][0]) <= 65338:
                                                continue
                                          else:
                                                token_with_kanji = parsed_txt[i].split('\t')
                                                if len(token_with_kanji) >= 12:
                                                      if not token_with_kanji[12] == '外':
                                                            reading = '*' + reading
                                                            kanji_list.append(reading)
                                                            kanji_counter += 1
                                                      else:
                                                            continue
                                                if len(token_with_kanji) < 12:
                                                      reading = '*' + reading    
                                                      kanji_list.append(reading)
                                                      kanji_counter += 1
                                                #print(reading)
                              else:
                                    continue
            if(lines_counter % 5000 == 0):
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
      path = '/home/anna/DH_research_2019-20/Source_test'
      files = os.listdir(path)
      for filename in files:
            if not filename.endswith('.txt'):
                  continue
            raw_file = open_file(path, filename)
            clean_txt = clean_the_text(raw_file)
            parsed_txt = parse_the_text(clean_txt)
            write_result_tsv(filename, parsed_txt)
            count_katakana(parsed_txt)
            count_romaji(parsed_txt)
            count_kanji(parsed_txt)
            
if __name__ == '__main__':
      main()
