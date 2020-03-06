import re
import MeCab

def open_the_file(filename):
      with open (filename, 'r', encoding = 'Shift-JIS') as openfile:
            raw_txt = openfile.read()
      return raw_txt

def clean_the_file(raw_file):
      step_1 = re.sub ('(----------).+(---------)', '', raw_file, flags=re.DOTALL) #очищаю от условных обозначений в начале
      step_2 = re.sub ('《.+?》', '', step_1)  #очищаю от фуриганы
      clean_txt = re.sub ('(底本：「).+?(ボランティアの皆さんです。)', '', step_2, flags=re.DOTALL) #очищаю от метаданных
      return clean_txt

def parse_the_text(clean_file):
      m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
      parsed_txt = m.parse(clean_file)
      return parsed_txt

def write_the_file(parsed_txt):
      fw = open("parsed_txt.txt", "w", encoding = "utf-8")
      fw.write("{}".format(parsed_txt))
      fw.close()

def main():
      raw_file = open_the_file('Source_for_research/majutsu.txt')
      clean_file = clean_the_file(raw_file)
      parsed_txt = parse_the_text(clean_file)
      fw = write_the_file(parsed_txt)

if __name__ == '__main__':
      main()
