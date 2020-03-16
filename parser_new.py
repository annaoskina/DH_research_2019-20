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
      step_3 = re.sub('※［＃「均のつくり」、第3水準1-14-75］', '', step_2)
      clean_txt = re.sub('(底本：「).+?(ボランティアの皆さんです。)', '', step_3, flags=re.DOTALL) #очищаю от метаданных
      return clean_txt

def parse_the_text(clean_txt):
      m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
      parsed_txt = m.parse(clean_txt)
      parsed_txt = parsed_txt.replace('\t', ',')
      parsed_by_words = parsed_txt.split('\n')
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
      for token in parsed_txt:
            token = token.split(',')
            if '外' in token[12]:
                  all_gairaigo += 1
                  gairaigo = gairaigo.append(token[0])
                  regex1 = '[ァ-・ヽヾ゛゜ー]'
                  regex2 = '[Ａ-ｚ]'
                  regex3 = '[U+4E00..U+62FF][U+6300..U+77FF][U+7800..U+8CFF][U+8D00..U+9FFF]'
                  if re.search(regex1, token[0]):
                        katakana_words += 1
                        katakana = katakana.append(token[0])
                  if re.search(regex2, token[0]):
                        romaji_words += 1
                        romaji = romaji.append(token[0])
                  if re.search(regex3, token[0]):
                        kanji_words += 1
                        kanji = kanji.append(token[0])
      print(katakana_words, romaji_words, kanji_words)
      print(katakana, romaji, kanji)

def write_the_file(parsed_txt):
      fw = open("parsed.txt", 'w', encoding = 'utf-8')
      fw.write("{}".format(parsed_txt))
      fw.close()

def main():

      raw_file = open_the_file('Source_for_research/majutsu.txt')
      clean_txt = clean_the_text(raw_file)
      parsed_txt = parse_the_text(clean_txt)
      #test = write_the_file(parsed_txt)
      count = count_loan_words(parsed_txt)

if __name__ == '__main__':
      main()
