import re

def open_the_file (filename):
      with open (filename, 'r', encoding = 'Shift-JIS') as openfile:
            raw_txt = openfile.read()
      return raw_txt

def clean_the_file (txt1):
      step_1 = re.sub ('(----------).+(---------)', '', txt1, flags=re.DOTALL) #очищаю от условных обозначений в начале
      step_2 = re.sub ('《.+》', '', step_1)  #очищаю от фуриганы
      clean_txt = re.sub ('(底本：「).+?(ボランティアの皆さんです。)', '', step_2, flags=re.DOTALL) #очищаю от метаданных
      return clean_txt

def main():
      txt1 = open_the_file('Source_for_research/majutsu.txt')
      txt2 = clean_the_file(txt1)
      print(txt2)

if __name__ == '__main__':
      main()
      

