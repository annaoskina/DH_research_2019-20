import re
import MeCab
import csv

def open_the_file(filename):
      with open (filename, 'r', encoding = 'Shift-JIS') as openfile:
            raw_txt = openfile.read()
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
      fw = open("parsed.tsv", 'w', encoding = 'utf-8')
      fw.write("{}".format(parsed_txt))
      fw.close()
      parsed_by_words = parsed_txt.split('\n')
      #print(parsed_by_words)
      return parsed_by_words

def count_loan_words(parsed_txt):
      all_gairaigo = 0
      gairaigo = []
      katakana_words = 0
      katakana = []
      romaji_words = 0
      romaji = []
      kanji_words = 0
      kanji = []
      lines = 0
      for token in parsed_txt:
            lines += 1
            token = token.split('\t')
            if len(token) > 12:
                  if '外' in token[12]:
                        all_gairaigo += 1
                        gairaigo.append(token[0])
                        if 65 <= ord(token[0][0]) <= 122:
                              romaji_words += 1
                              romaji.append(token[0])
                        if 12450 <= ord(token[0][0]) <= 12531:
                              katakana_words += 1
                              katakana.append(token[0])
                        else:
                              kanji_words += 1
                              kanji.append(token[0])
                  if '固' in token[12]:
                        if 65 <= ord(token[0][0]) <= 122:
                              all_gairaigo += 1
                              romaji_words += 1
                              romaji.append(token[0])
                        if 12450 <= ord(token[0][0]) <= 12531:
                              all_gairaigo += 1
                              katakana_words += 1
                              katakana.append(token[0])
            if 1 < len(token) <= 7:
                  #print(token)
                  if 65 <= ord(token[0][0]) <= 122:
                        all_gairaigo += 1
                        romaji_words += 1
                        romaji.append(token[0])
                  if 12450 <= ord(token[0][0]) <= 12531:
                        all_gairaigo += 1
                        katakana_words += 1
                        katakana.append(token[0])
      print(lines, all_gairaigo, katakana_words, romaji_words, kanji_words)
      print(katakana, romaji, kanji)

def write_the_file(parsed_txt):
      fw = open("parsed.txt", 'w', encoding = 'utf-8')
      fw.write("{}".format(parsed_txt))
      fw.close()

def main():
      #raw_file = open_the_file('Source_for_research/majutsu.txt')
      #raw_file = open_the_file('Source_for_research/vita_sexualis.txt')
      raw_file = open_the_file('Source_for_research/maihime.txt')
      clean_txt = clean_the_text(raw_file)
      print(clean_txt)
      parsed_txt = parse_the_text(clean_txt)
      #test = write_the_file(parsed_txt)
      count = count_loan_words(parsed_txt)
      #tsv = write_tsv(parsed_txt)

if __name__ == '__main__':
      main()
