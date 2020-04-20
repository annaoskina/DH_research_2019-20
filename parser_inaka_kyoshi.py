import re
import MeCab
import csv
import os

def open_the_file(filename):
      with open('/home/anna/DH_research_2019-20/{}'.format(filename), 'r', encoding = 'Shift-JIS') as f:
                  raw_txt = f.read()
      return raw_txt

def clean_the_text(raw_file):
      step_1 = re.sub('(----------).+(---------)', '', raw_file, flags=re.DOTALL) #очищаю от условных обозначений в начале
      step_2 = re.sub('《.+?》', '', step_1)  #очищаю от фуриганы
      step_3 = re.sub('［＃.+?］', '', step_2)
      clean_txt = re.sub('(底本：「).+?(ボランティアの皆さんです。)', '', step_3, flags=re.DOTALL) #очищаю от метаданных
      return clean_txt

def parse_the_text(clean_txt):
      m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
      parsed_txt = m.parse(clean_txt)
      parsed_txt = parsed_txt.replace(',', '\t')
      return parsed_txt

def count_loan_words(parsed_txt):
      gairaigo_counter = 0
      katakana_counter = 0
      katakana_array = ['katakana']
      katakana_list = []
      romaji_counter = 0
      romaji_array = ['romaji']
      romaji_list = []
      kanji_counter = 0
      kanji_array = ['kanji']
      kanji_list = []
      lines_counter = 0
      parsed_by_words = parsed_txt.split('\n')
      for token in parsed_by_words:
            lines_counter += 1
            token = token.split('\t')
            if len(token) > 12:
                  if '外' in token[12]:
                        gairaigo_counter += 1
                        if 65 <= ord(token[0][0]) <= 122:
                              romaji_counter += 1
                              romaji_list.append(token[0])
                        elif 12450 <= ord(token[0][0]) <= 12538:
                              katakana_counter += 1
                              katakana_list.append(token[0])
                        elif 12352 <= ord(token[0][0]) <= 12447:
                              continue
                        elif 48 <= ord(token[0][0]) <= 57:
                              continue
                        else:
                                    kanji_counter += 1
                                    kanji_list.append(token[0])
                  if '固' in token[12]:
                        if 65 <= ord(token[0][0]) <= 122:
                              gairaigo_counter += 1
                              romaji_counter += 1
                              romaji_list.append(token[0])
                        if 12450 <= ord(token[0][0]) <= 12538:
                              gairaigo_counter += 1
                              katakana_counter += 1
                              katakana_list.append(token[0])
            if 1 < len(token) <= 7:
                  if 65 <= ord(token[0][0]) <= 122:
                        gairaigo_counter += 1
                        romaji_counter += 1
                        romaji_list.append(token[0])
                  if 12450 <= ord(token[0][0]) <= 12538:
                        gairaigo_counter += 1
                        katakana_counter += 1
                        katakana_list.append(token[0])
            if(lines_counter % 5000 == 0):
                  kanji_array.append(kanji_counter)
                  romaji_array.append(romaji_counter)
                  katakana_array.append(katakana_counter)
                  kanji_counter = 0
                  romaji_counter = 0
                  katakana_counter = 0
      katakana_array.append(katakana_counter)
      kanji_array.append(kanji_counter)
      romaji_array.append(romaji_counter)
      print('words total =\t', lines_counter)
      print(katakana_list, kanji_list, romaji_list)
      #print('katakana =\t', katakana_array, '\nkanji =\t\t', kanji_array, '\nromaji =\t', romaji_array)
      return katakana_array, kanji_array, romaji_array

def main():
      files = os.listdir('/home/anna/DH_research_2019-20/Source_to_test')
      for file in files:
            if not file.endswith('.txt'):
                  continue
            with open('/home/anna/DH_research_2019-20/Source_to_test/{}'.format(file), 'r', encoding = 'Shift-JIS') as f:
                  print('\n', file)
                  raw_file = f.read()
                  clean_txt = clean_the_text(raw_file)   
                  parsed_txt = parse_the_text(clean_txt)
                  #with open('/home/anna/DH_research_2019-20/Files_tsv/{}.tsv'.format(file), 'w', encoding = 'utf-8') as fw:
                  #      fw.write("{}".format(parsed_txt))
                  result = count_loan_words(parsed_txt)
                  print(result)
                 # with open('/home/anna/DH_research_2019-20/Results/{}.csv'.format(file), 'w', encoding = 'utf-8', newline = '') as csv_file:
                  #      writer = csv.writer(csv_file, delimiter = ',')
                   #     for line in result:
                    #          writer.writerow(line)

if __name__ == '__main__':
      main()
