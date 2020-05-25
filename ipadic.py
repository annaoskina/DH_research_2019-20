from pymecab.pymecab import PyMecab
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

def parse_with_ipadic(clean_txt):
      mecab = PyMecab()
      tokenized_txt = []
      for token in mecab.tokenize(clean_txt):
            tokenized_txt.append(token)
      #print(len(tokenized_txt))
      return tokenized_txt

def count_romaji(parsed_txt):
      romaji_counter = 0
      romaji_list = []
      romaji_array = []
      lines_counter = 0
      for token in parsed_txt:
            lines_counter += 1
            if token[0]:
                  if 65 <= ord(token[0][0]) <= 122: #включаю латиницу half-width (H)
                        romaji_counter += 1
                        romaji_list.append(token[0])
                  if 65313 <= ord(token[0][0]) <= 65338: #включаю латиницу full-width (Ｈ)
                        romaji_counter += 1
                        romaji_list.append(token[0])
                  if(lines_counter % 5000 == 0):
                        romaji_array.append(romaji_counter)
                        romaji_counter = 0
      romaji_array.append(romaji_counter)
      #print(romaji_list)
      print(len(romaji_list))
      print(romaji_array)
      return romaji_array
            

def main():
      path = '/home/anna/DH_research_2019-20/Source_test'
      files = os.listdir(path)
      for filename in files:
            if not filename.endswith('.txt'):
                  continue
            raw_file = open_file(path, filename)
            clean_txt = clean_the_text(raw_file)
            parsed_txt = parse_with_ipadic(clean_txt)
            count_romaji(parsed_txt)
            
if __name__ == '__main__':
      main()
